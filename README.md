# SynFB
<p>SynFB it's thinked for running on a Linux o.s. It's a software for detect every 40sec the IP who generate a lot of requests with flag (for default the limit it's setted on 50 SYN) SYN setted.
If one IP exceed the limit setted, SynFB will send an alert e-mail to the administrator</p>
<h2>Pre-requisites</h2>
<ul>
    <li>Debian based linux distro recommended. But it can be run on all distros that have shell commands available in the following line:
        <br><code>netstat -ano | grep SYN_RECV |  awk {'print $4,$5'} | awk -F: {'print $1,$2'} | sort -k 3 | uniq -c | sort -k 1 | tail -1</code></li>
    <li>Python 2.7</li>
</ul>
