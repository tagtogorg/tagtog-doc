---
layout: page
title: SysAdmin
sidebar_link: true
id: sysadmin-onpremises
toc: true

tagtog_domain: https://www.tagtog.net
request_auth_token_endpoint: /-sysadmin/request-auth-token
---

<div class="two-third-col" markdown="1">

<br>

Accessible only in tagtog OnPremises, the <strong>SysAdmin page</strong> lets you manage tasks at the system level.
</div>

<div class="two-third-col">
  <h2>How to access</h2>
  <p>Go to your root domain set for tagtog (either an IP or a custom domain) and access <code>/-sysadmin</code> relative path. For example: <code>https://example.org/-sysadmin</code>. You will be prompted with a basic authentication panel, to enter the fields:</p>
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
  <h2>User Management</h2>
  <p>The admin panel displays a list of the users registered in the instance. You can:</p>
  <p class="list-item" markdown="1"><span class="list-item-1"></span>**Create new accounts**: generate a registration link to share with others or to use oneself</p>
  <p class="list-item" markdown="1"><span class="list-item-2"></span>**Edit accounts**: edit the users' accounts main information, namely, username, email, and password. 📝</p>
  <p class="list-item" markdown="1"><span class="list-item-3"></span>**Remove accounts**: remove users that for example do not use anymore the application. Remove a user from the system by clicking on the remove button {% include inline-image.html name="editor-doc-remove.PNG" %}.</p>
  <p class="list-item" markdown="1"><span class="list-item-4"></span>**Revoke all auth tokens**: remove all existing token-based logins and registration links</p>
</div>
<div class="two-third-col">
  <h2>Roles and permissions</h2>
  <p>In the admin panel you can find a permission matrix where you can check &amp; modify the permissions of existing roles or to create custom roles. After, these roles can be assigned to users at project level.</p>
  <p>All the <strong>permissions are explained here</strong>: <a title="tagtog - Multi-user annotation - permissions" href="collaboration.html#permissions">Multi-user annotation - permissions</a></p>
  <p>By default there are three roles in the system: <code>admin</code>, <code>supercurator</code> and <code>reader</code>. The permissions for these default roles cannot be modified. Admin role cannot be removed (the creator of a project, the owner, will always have this role assigned). The roles supercurator and reader can be removed. If you want to modify their permissions, you should remove the role, and create a new role with the same name.</p>
  <p>To create a new role simply click on <i>Add new role</i>. To change a permission, you should click on the corresponding checkbox. If you hover on the permission name or on a role name, a description of the permission or the role will show up.</p>
  <p>For each role, you can perform three actions:</p>
  <p class="list-item"><span class="list-item-1"></span>{% include inline-image.html name="edit_pencil.png" width="28" %}<strong>Edit its name/description</strong></p>
  <p class="list-item"><span class="list-item-2"></span>{% include inline-image.html name="editor-doc-remove.PNG" width="23" %}<strong>Remove it</strong>. If you remove a role, you should indicate which is the role that will be assigned to all the users once their original role is removed.</p>
  <p class="list-item"><span class="list-item-3"></span><strong>Change its permissions</strong></p>

  {% include image.html name="role_matrix.png"  width="650" caption="Permission matrix. In this example, in addition to the default roles, there is a new role myNewRole" %}
</div>
<div class="one-third-col">
  <div class="message">
    Depending on your <a href="https://www.tagtog.net/-plans" title="tagtog - plans">plan</a>, you might not see this feature.
  </div>
  <div class="message">
    <strong>Any change is reflected immediately</strong> across all the projects in the system.
  </div>
  <div class="message">
    When a role is removed, all the users under this role are assigned to another role (chosen by the sysadmin).
  </div>
</div>

<div class="two-third-col" markdown="1">

## Single Sign-On (SSO)

</div>

<div class="two-third-col" markdown="1">

### OpenID Connect (OIDC)

You can link to tagtog your **OpenID Connect Provider** (e.g. KeyCloak, Okta, AWS Cognito, Microsoft, Salesforce.com, etc.). With this, your users will be able to login into tagtog seamlessly (with the authentication mechanism they already know).

#### Setup OIDC

First of all, you must define a client for tagtog in your OIDC Provider. This client's access type should be _"Confidential"_. This will generate a secret (a password) that you later pass on to tagtog. Moreover, of course, the root URL of the tagtog client should be the domain of your tagtog OnPremises instance.

Then, there are 3 variables that tagtog must know about your OIDC Provider and the client you just defined, namely:

* `wellknownDiscoveryUrl`: this is the standard `.well-known/openid-configuration` endpoint URL of your OIDC Provider.
* `clientId`: this is the name you give in your Provider to tagtog. Typically, you should always call this "tagtog".
* `clientSecret`: the secret associated to the tagtog client in your OIDC Provider.

Additionally, you must decide on the value of this tagtog-specific variables:

* `usersThatCanBeCreatedAutomaticallyIfNotFoundInTagtog`: tagtog OIDC integration lets you choose whether users of your authentication system should have a tagtog account created automatically if they login on tagtog or not. The possible values are:
  * `""` (none): no users will be created automatically unless they exist already on tagtog.
  * `"*"` (all): all users of your OIDC system will be created automatically on tagtog if they log in and they have no associated tagtog account yet.
  * comma-separated list of usernames (e.g. "John,Maria,Peter"): usernames in your OIDC system of users that can be created automatically on tagtog if they log in and they have no associated tagtog account yet.

Finally, the way you pass these variables to tagtog is by using java dynamic properties. Example:

```shell
export TAGTOG_JAVA_OPTS="${TAGTOG_JAVA_OPTS} \
-Dapplication.auth.openid.wellknownDiscoveryUrl=http://mySSO:8080/auth/realms/master/.well-known/openid-configuration \
-Dapplication.auth.openid.clientId=tagtog \
-Dapplication.auth.openid.clientSecret=64934247-ea33-4ec7-8e86-197ea9be3417 \
-Dapplication.auth.openid.usersThatCanBeCreatedAutomaticallyIfNotFoundInTagtog= \
"

# Then, restart tagtog as normally
./tagtog_on_premises restart latest $TAGTOG_HOME
```

</div>

<div class="two-third-col">
  <h3>Auth Tokens</h3>
  <p markdown="1">An alternative SSO system on tagtog is based on **authentication tokens**. These can only be generated by the sysadmin (via API). The sysadmin can then have injected, in a simple reverse proxy server or just simple URL redirections, the corresponding authentication token that distinctively grant one user to login. The sysadmin can keep an internal map of reusable tokens or generate them on-demand programatically any time a login access is required (see below the `useOnce` API parameter). All auth tokens can easily be deleted at any time (see above: [Revoke all auth tokens](#user-management)).</p>

  <h4>API to request auth token</h4>

  <table style="width:100%;white-space:nowrap;">
    <tr>
      <td><strong>Endpoint</strong></td>
      <td><code>{{ page.request_auth_token_endpoint }}</code></td>
    </tr>
    <tr>
      <td><strong>Method</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Output</strong></td>
      <td>String, the auth token</td>
    </tr>
  </table>

  <p markdown="1">**Input Parameters**</p>

    <p>Defined as JSON parameters:</p>

    <table style="width:100%;">
      <tr>
        <th>Name</th>
        <th>Default</th>
        <th>Example</th>
        <th>Description</th>
      </tr>
      <tr>
        <td><code>toUsername</code> (String)</td>
        <td>-</td>
        <td><em>yourUsername</em></td>
        <td>The user's username you grant the authentication to.</td>
      </tr>
      <tr>
        <td><code>expirationHours</code> (Int)</td>
        <td>-1 (meaning, no expiration)</td>
        <td>24</td>
        <td>The expiration in hours for the token to still be usable. Leave undefined or otherwise write a negative number to not have any expiration (meaning the token is valid until removed).</td>
      </tr>
      <tr>
        <td><code>useOnce</code> (Boolean)</td>
        <td>false</td>
        <td>true</td>
        <td>Besides the expiration, with this parameter you can decide whether the token can be used only once (true) or not (false, i.e., multiple times until the token is removed or expires).</td>
      </tr>
    </table>

</div>

<div class="two-third-col" markdown="1"> <!-- Opens main section: two-third-cold div -->
  **Coding examples**

<div id="tabs-container">
<ul class="tabs-menu">
  <li class="current"><a href="#tab_api_request_auth_token_curl">cURL</a></li>
  <li><a href="#tab_api_request_auth_token_httpie">HTTPie</a></li>
</ul>
<div class="tab">
<div id="tab_api_request_auth_token_curl" class="tab-content" style="display: block" markdown="1">
```shell
curl -u LICENSE_NAME:LICENSE_KEY -X POST -H "Content-Type: application/json" '{{ page.tagtog_domain }}{{ page.request_auth_token_endpoint }}' \
-d '{"toUsername": "yourUsername", "useOnce": true, "expirationHours": 48}'
# Example output: bbfd-33878148-6062-4934-a507-af4962753c8f
```
</div>

<div id="tab_api_request_auth_token_httpie" class="tab-content" markdown="1">
```shell
http --auth LICENSE_NAME:LICENSE_KEY POST '{{ page.tagtog_domain }}{{ page.request_auth_token_endpoint }}' toUsername=yourUsername useOnce:=false
# Example output: 6f0d-90c2386a-8a33-4ad1-bd19-d4d35ad06f96
```
</div>

</div>
</div>

</div> <!-- Closes main section: two-third-cold div -->


<div class="two-third-col" markdown="1">

#### How to use an auth token

Once you have an auth <code>token</code>, use it in a simple GET request to login with the associated-granted user. To the request also add a <code>redirectTo</code> (<a href="https://meyerweb.com/eric/tools/dencoder/">url-encoded</a>) parameter to indicate where to redirect to. You must add these parameters to the <code>/</code> (root endpoint) of your tagtog's installation domain.

Example: `{{ page.tagtog_domain }}/?redirectTo=https%3A%2F%2Fwww.tagtog.net%2F-datasets&token=bbfd-33878148-6062-4934-a507-af4962753c8f`
</div> <!-- Closes main section: two-third-cold div -->


<!-- <div class="two-third-col"> -->
<!-- <br/><hr/><br/> -->

<div class="two-third-col" markdown="1">

## Tighter authorization

Sometimes you want to have a tighter control about what the users and visitors of your system are allowed to do. You can configure the following authorization controls **using java dynamic properties**. Specifically, you must set the environment variable `TAGTOG_JAVA_OPTS` with the desired configuration values as described for each point below.


### Disallow visitors to create accounts

Sometimes you do not want to allow visitors to your tagtog installation creating accounts themselves. In such a case, the sysadmin is responsible to create the accounts for all the users.

Set `application.canVisitorsCreateAccounts` to `false` (the default is _true_). Example:

```shell
export TAGTOG_JAVA_OPTS="${TAGTOG_JAVA_OPTS} -Dapplication.canVisitorsCreateAccounts=false";
./tagtog_on_premises restart latest $TAGTOG_HOME
```


### Disallow users to change their account details

In such a case, the sysadmin is responsible to edit the account details of the users.

Set `application.canUsersEditTheirAccounts` to `false` (the default is _true_). Example:

```shell
export TAGTOG_JAVA_OPTS="${TAGTOG_JAVA_OPTS} -Dapplication.canUsersEditTheirAccounts=false";
./tagtog_on_premises restart latest $TAGTOG_HOME
```


### Disallow users to recover their passwords using the "Forgot Password?" email

In such a case, the sysadmin is entirely responsible for the users' passwords.

Set `application.canUsersRequestForgotPassword` to `false` (the default is _true_). Example:

```shell
export TAGTOG_JAVA_OPTS="${TAGTOG_JAVA_OPTS} -Dapplication.canUsersRequestForgotPassword=false";
./tagtog_on_premises restart latest $TAGTOG_HOME    
```

</div> <!-- Ends markdown -->
