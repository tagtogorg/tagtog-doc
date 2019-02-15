---
layout: page
title: SysAdmin On-Premises
sidebar_link: true
id: sysadmin-premises
toc: true
---

<div class="page-section">
  <div class="two-third-col">
    <h2>Introduction</h2>
    <p>In On-Premises instances, using the <strong>SysAdmin page</strong> you can perform different management tasks at the system level.</p>
  </div>
  <div class="one-third-col">
    <div class="message">
      This panel is only accessible in <strong>on-premises</strong> instances.
    </div>
  </div>

  <div class="two-third-col">
    <h2>How to access</h2>
    <p>Go to your root domain set for tagtog (you probably use directly the IP or a custom domain) and access <code>/-sysadmin</code> relative path. For example: <code>https://nlp.cia.com/-sysadmin</code>. You will be prompted with a basic authentication panel, to enter the fields:</p>
    <p class="list-item"><span class="list-item-1"></span><strong>Username</strong>: use the subscription license name</p>
    <p class="list-item"><span class="list-item-2"></span><strong>Password</strong>: use the subscription license key</p>

    {% include image.html name="sysadmin-onpremises-users.png"  caption="Username, email address, and registration date." %}
  </div>
  <div class="one-third-col">
    <div class="message">
      <strong>License information</strong> is sent to you by email by the tagtog team when you first purchased the on-premises software.
    </div>
  </div>

  <div class="two-third-col">
    <h2>Features</h2>

    <h3>User Management</h3>
    <p>The admin panel displays a list of the users registered in the instance. You can:</p>

    <p class="list-item" markdown="1"><span class="list-item-1"></span>**Create new accounts**: generate a registration link to share with others or to use oneself</p>
    <p class="list-item" markdown="1"><span class="list-item-2"></span>**Edit accounts**: edit the users' accounts main information, namely, username, email, and password. 📝</p>
    <p class="list-item" markdown="1"><span class="list-item-3"></span>**Remove old accounts**: remove users that for example do not use anymore the application. Remove a user from the system by clicking on the remove button {% include inline-image.html name="editor-doc-remove.PNG" %}.</p>
    <p class="list-item" markdown="1"><span class="list-item-4"></span>**Revoke all auth tokens**: remove all existing token-based logins and registration links</p>

    <h3>Tighter authorization</h3>

      <h4>Do not allow visitors to create accounts</h4>

      <p markdown="1">For a tight control, sometimes you do not want to allow visitors to your tagtog installation creating accounts themselves. In such a case, the admin is responsible to create the accounts for all the users.</p>

      <p markdown="1">To disable visitors to create accounts, you need to set the java dynamic property `application.canVisitorsCreateAccounts` to `false` (the default is _true_) in the global environment variable `TAGTOG_JAVA_OPTS`, such like:</p>

      <p markdown="1">
      ```
      export TAGTOG_JAVA_OPTS="-Dapplication.canVisitorsCreateAccounts=false"; ./tagtog_on_premises restart latest $PWD/tagtog_home    
      ```
      </p>
  </div>
  <div class="one-third-col">
  </div>
</div>
