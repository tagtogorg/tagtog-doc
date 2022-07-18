---
layout: page
title: SysAdmin
sidebar_link: true
id: sysadmin-onpremises
toc: true

tagtog_domain: https://www.tagtog.com
request_auth_token_endpoint: /-sysadmin/request-auth-token
onpremises_tagtog_domain: https://tagtog.example.org

openid_login_btn: _"Log in with OpenID"_
openid_login_url: /-login-openid-connect
---

<div class="two-third-col" markdown="1">

<br>

Accessible only in tagtog OnPremises, the <strong>SysAdmin page</strong> lets you manage tasks at the system level.
</div>

<div class="two-third-col">
  <h2>How to access</h2>
  <p>Go to your root domain set for tagtog (either an IP or a custom domain) and access the <code>/-sysadmin</code> relative path; for example: <code>{{page.onpremises_tagtog_domain}}/-sysadmin</code>. You will be prompted with a basic authentication panel, to enter the fields:</p>
  <p class="list-item"><span class="list-item-1"></span><strong>Username</strong>: use the subscription license name.</p>
  <p class="list-item"><span class="list-item-2"></span><strong>Password</strong>: use the subscription license key.</p>
</div>
<div class="one-third-col">
  <div class="message">
    <strong>License information</strong> is sent to you by email by the tagtog team when you purchase your tagtog OnPremises subscription.
  </div>
</div>

<div class="two-third-col">
  <h2>User Management</h2>

</div>

<div class="two-third-col" markdown="1">

### License model: floating seats

In OnPremises, your tagtog license allows you a maximum number of **active** users (seats). On top, in the [tagtog ENTERPRISE plan](https://www.tagtog.com/-plans#ONPREMISES), you can have in your system more users created. For example, let's say you have a tagtog ENTERPRISE license for 25 annotators. In this case, you could have more users registered than 25, but only 25 of them can be **active**. The rest of the users must be **inactive**.

<div class="img-with-caption" align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/aYsouRrJ_Uk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <p>Floating seats: flexibly assign & re-assign your free active seats.</p>
</div>

**Active** users are regular users, which can use the system.

**Inactive** users, however, cannot log in. Moreover, their annotations cannot be modified.

Changing the "is active" status of your users is always possible and easily done in the [user panel](#user-panel).

**Your benefit**: if your team members rotate, leave, or change, you don't have to remove their tagtog users. You can just deactivate them. Then, as long as your inactive users remain invited to the projects, all their data will still be there. Moreover, if you activate their tagtog users again, they will be able to pick up their work. This gives you more flexibility and peace of mind.

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/users-summary-info.png" width="40%" alt="Screenshot: panel informing about users in the system & limit of active users" />
  <p>Panel informing about users in the system & limit of active users.</p>
</div>

</div>


<div class="two-third-col">

  <h3>User panel</h3>
  <p>The user panel displays a list of the users registered in the instance. You can:</p>
  <p class="list-item" markdown="1"><span class="list-item-1"></span>**Create new accounts**: you can add a user account directly in the sysadmin panel.</p>
  <p class="list-item" markdown="1"><span class="list-item-2"></span>**Edit accounts**: edit the users' accounts main information. Edit a user from the system by clicking on the edit button {% include inline-image.html name="edit_pencil.png" width="20" %}</p>
  <p class="list-item" markdown="1"><span class="list-item-3"></span>**Remove accounts**: remove users that for example do not use anymore the application. Remove a user from the system by clicking on the remove button {% include inline-image.html name="editor-doc-remove.PNG" %}.</p>

  <p>Fields in the table:</p>
  <p class="list-item" markdown="1"><span class="list-item-1"></span>**Count**: index of the user.</p>
  <p class="list-item" markdown="1"><span class="list-item-2"></span>**Is active**: flag to indicate whether the user is [active or not](#license-model-floating-seats).</p>
  <p class="list-item" markdown="1"><span class="list-item-3"></span>**Username**</p>
  <p class="list-item" markdown="1"><span class="list-item-4"></span>**Email**</p>
  <p class="list-item" markdown="1"><span class="list-item-5"></span>**Creation date**: date the user account was created in.</p>
  <p class="list-item" markdown="1"><span class="list-item-6"></span>**Can create projects**: flag to indicate whether the user can create projects or not. Users who cannot create projects, can only work in projects they are invited to. This is useful when you want in your organization only one or a small set of accounts owning all the projects. This makes control & management easier.</p>
  <p class="list-item" markdown="1"><span class="list-item-7"></span>**Has password**: accounts with `Basic authentication` have password. `Single sign-on` accounts don't have password within the application.</p>

  {% include image.html name="sysadmin/users-panel.png" caption="User panel: inspect, create, update, and delete users." %}

</div>

<div class="two-third-col">
  <h3>Create a new user</h3>
  <p markdown="1">To create a new user using the sysadmin user panel, click on **+ Add new user**. A form will show up with the following fields:</p>
  <p class="list-item" markdown="1"><span class="list-item-1"></span>**Account type**: `Basic authentication` (regular tagtog account with username and password) or `Single sign-on` ([documentation](on-premises-sysadmin.html#single-sign-on-sso)). <br/> In the user panel, accounts with `Basic authentication` with the flag `Has Password`   </p>
  <p class="list-item" markdown="1"><span class="list-item-2"></span>**Username**: the new user's username.</p>
  <p class="list-item" markdown="1"><span class="list-item-3"></span>**Email**: the new user's email.</p>
  <p class="list-item" markdown="1"><span class="list-item-4"></span>**Password**: the password of the new user. The user can later change the password. This field is only required for accounts with `Basic authentication`.</p>
  <p class="list-item" markdown="1"><span class="list-item-5"></span>**Can create projects**: flag to indicate whether the new user can create tagtog projects or not.</p>
   <p class="list-item" markdown="1"><span class="list-item-6"></span>**Is active**: flag to indicate whether the new user will be [active or not](#license-model-floating-seats).</p>
</div>
<div class="one-third-col">
  {% include image.html name="sysadmin/user-create-or-update.png" caption="Create &amp; edit user view" width="90%" %}
</div>

<div class="two-third-col">
  <h3>Create a new user by registration link</h3>
  <p markdown="1">You can generate a registration link to share with others or to use oneself. Anyone who has this link and access to the system, can create a regular user account signing up in the application.</p>
</div>


<div class="two-third-col" markdown="1">

## Teams Management

_tagtog Teams_ allow you to group users by their responsibilities, department, guest status, etc.

Then, you can [add the teams directly to your projects](projects.html#add-members-teams-to-your-project) (rather than adding the individual members one by one). **This makes user control much easier**. For example, with teams you can change in one go, in a project, the role of all team users'.

On the SysAdmin page, you have all options to manage the teams of your organization. Of course, you can inspect your teams, create new ones, update them, and/or delete them.

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/teams-panel.png" alt="Screenshot: teams panel" />
  <p>Teams panel: inspect, create, update, and delete teams.</p>
</div>


### Creating & updating a team

To create (or update) a team just:

* define the team's name,
* set an optional description,
* and select the desired users. To select users, just click on their usernames or search by their usernames (or by email address).

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/teams-create-update-team1.png" width="50%" align="center" alt="Screenshot: popup to create or update a team" />
  <p>Create a team, by choosing its name and users.</p>
</div>


### Teams & Projects are always in sync

[Once a team (and therefore its users) is added to a project](projects.html#add-members-teams-to-your-project), the team's users and the project will always be in _sync_. This is better explained with an example:

* Say you you have created a team _"Team1"_ with users: _"userA"_, _"userB"_, and _"userC"_.
* Then you add _"Team1"_ to your project _"DemoProject"_ with some role (for instance, _"curator"_).

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/teams-add-team1-to-project-c.png" width="50%" align="center" alt="Screenshot: adding a team to your project" />
  <p>Adding a team to your project (with some role), will also add all the team's users to your project (with default same role).</p>
</div>

* This will mean that _"userA"_, _"userB"_, and _"userC"_ will be added, all at once, to _"DemoProject"_ (with role _"curator"_).

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/teams-team1-in-project-b.png" width="50%" align="center" alt="Screenshot: show team in project" />
  <p>Read the teams &amp; members from your project.</p>
</div>

* Later on, for instance, you add another user to your team, _"userD"_, and remove from the team the user _"userC"_.

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/teams-team1-updated.png" width="40%" align="center" alt="Screenshot: update your team" />
  <p>You can update your teams at any time.</p>
</div>

* This will mean that, automatically, _"userD"_ will also be added to _"DemoProject"_ (with role _"curator"_), and that _"userC"_ will be removed from the project. Of course, since _"userA"_ and _"userB"_ were not affected, they will remain in the project.

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/teams-team1-in-project-updated-b.png" width="50%" align="center" alt="Screenshot: show your updated team in project" />
  <p>Your teams &amp; projects are always in sync.</p>
</div>


### Deleting a team

To delete a team just click on its associated removal button (the trash can icon). You will be asked in a 2nd-step dialog to confirm that you do want to delete the team. On top, you can confirm or not the checkbox _"Remove the team's users from the projects they are assigned to"_:

* If you leave the checkbox unchecked, the team will be deleted from all associated projects. However, the team's users (if any) will remain in the respective projects, with the role they already had.
* If you check the checkbox, the team and also the the team's users will be deleted from all associated projects.

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/teams-delete-b.png" width="90%" align="center" alt="Screenshot: dialog to confirm deleting a team" />
  <p>You can delete teams, thus removing the teams from the associated projects, and also possibly the team's users.</p>
</div>

Important: **the removal of project members/teams cannot be undone!** Please make sure you have downloaded their annotations before, or that you have merged their annotations into the <code>master</code> version.


### Teams are flexible

With tagtog Teams, you can:

* **Add/update/delete the team' users at any moment**
* **Have in a project multiple teams**
* **Have one user belong to 2 or more teams, also in a project**
* **Define empty teams (that is, without users) and add them to projects**
* **Combine in a project individual members and teams**

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/teams-flexible-many.png" width="60%" align="center" alt="Screenshot: many projects in a team" />
  <p>Teams give you more tools to control your users' level of authorization.</p>
</div>

</div>


<div class="two-third-col">
  <h2>Roles &amp; Permissions</h2>
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
    Depending on your <a href="https://www.tagtog.com/-plans" title="tagtog - plans">plan</a>, you might not see this feature.
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

You can link to tagtog your **OpenID Connect Provider** (e.g. KeyCloak, Auth0, Okta, AWS Cognito, Microsoft, Salesforce.com, etc.). With this, your users will be able to login into tagtog seamlessly (with the authentication mechanism they already know).

#### OIDC: Setup

First of all, you must define a client for tagtog in your OIDC Provider:

* Define the client id (e.g. "tagtog").
* Of course, set the root URL of the tagtog client as the domain of your tagtog OnPremises instance.
* Enable the _"Authorization Code Flow"_ (also called "standard", or "server" authentication).
* The access type should be _"Confidential"_.
* The authentication method should be based on **client id & secret**.

Then, there are 3 variables that tagtog must know about your OIDC Provider and the client you just defined, namely:

* `wellknownDiscoveryUrl`: this is the standard `.well-known/openid-configuration` endpoint URL of your OIDC Provider.
* `clientId`: this is the name you give in your Provider to the tagtog client (e.g., again, "tagtog").
* `clientSecret`: the secret (password) associated to the tagtog client in your OIDC Provider.

Moreover, and optionally, you can also configure the following tagtog-specific variables:

* `usersThatCanBeCreatedAutomaticallyIfNotFoundInTagtog` (OPTIONAL; default=`""`): tagtog OIDC integration lets you choose whether users of your authentication system should have a tagtog account created automatically or not (that is, when they login on your Provider but do not have a tagtog account yet). The possible values are:
  * `""` (none): no users will be created automatically unless they exist already on tagtog.
  * `"*"` (all): all users of your OIDC system will be created automatically on tagtog if they log in and they have no associated tagtog account yet.
  * comma-separated list of emails (e.g. "John@example.org,Maria@example.org,Peter@example.org"): users' emails in your OIDC system of users that can be created automatically on tagtog if they log in and they have no associated tagtog account yet.
* `usernameClaim` (OPTIONAL; default=`preferred_username` or, if not existing, `sub`): the _claim_ (attribute) of your OIDC provider that you want to use for your users' usernames. In practice, this parameter is only relevant if you let your users' accounts to be created automatically if they don't exist on tagtog yet (see: `usersThatCanBeCreatedAutomaticallyIfNotFoundInTagtog`). If the accounts already exist on tagtog, they are primarily identified by their email address ([see below](#oidc-important-to-know)). In this case, the usernames can take any value ([with some restrictions](#oidc-important-to-know)). Note that you, as the sysadmin, can create the users first manually, associating them the email address registered in your OIDC Provider, and giving them an arbitrary username. Also note that, if you rely on this variable, you can use any custom attribute/claim of your OIDC Provider.
* `redirectTagtogRootUri` (OPTIONAL; default=originating host): by default when users successfully login on your OIDC Provider, they are redirected back to the originating host, which should be your tagtog OnPremises domain. Therefore, in most cases you should not set this variable. However, sometimes, due to redirections and having "docker-in-between" the originating host might not be read properly, or otherwise be wrongly set to the localhost. For these cases, use this variable. It should be the domain of your tagtog OnPremises domain; e.g. `{{page.onpremises_tagtog_domain}}` (please do not write a trailing forward slash, "/").

Finally, the way you pass these variables to tagtog is by using java dynamic properties. Example:

```shell
export TAGTOG_JAVA_OPTS="${TAGTOG_JAVA_OPTS} \
-Dapplication.auth.openid.default.wellknownDiscoveryUrl=https://mySSO:8443/auth/realms/master/.well-known/openid-configuration \
-Dapplication.auth.openid.default.clientId=tagtog \
-Dapplication.auth.openid.default.clientSecret=64934247-ea33-4ec7-8e86-197ea9be3417 \
-Dapplication.auth.openid.default.usersThatCanBeCreatedAutomaticallyIfNotFoundInTagtog= \
-Dapplication.auth.openid.default.usernameClaim=myCustomAttribute \
"

# Then, restart tagtog as normally
./tagtog_on_premises restart latest $TAGTOG_HOME
```

#### OIDC: Important to know

These are relevant aspects of the tagtog OIDC integration:

* **Scopes & claims**: tagtog's OIDC client (Relying Party) asks your OIDC Provider for only these 3 standard scopes: `openid, email, profile`.

  In particular, we only ask for the scope `profile` to get access to the `preferred_username` claim, might it be present. From the scope `email`, we only access the claims `email` and `email_verified` (if present).

  **Only mandatory are the claims `sub`** (from the scope `openid`) **and `email`**.

* **Users primary identification is by their email**. This means that the mapping between your users in your OIDC Provider and the tagtog registered users is based on the email claim/attribute. In pratical terms, this means that a user on tagtog with, for instance, username "A" and email "A@example.org", and a user on your Provider with different username "A-alt" but same email "A@example.org", represent the very same user.

* **Valid usernames follow the regex: `[a-zA-Z][a-zA-Z0-9-]{0,39}`**. Trying to add users with an invalid username, either manually or "automatically" (upon user OIDC login), will throw an error. If you have good reasons to make the username regex more flexible, [please let us know](https://www.tagtog.com/#contact).


#### OIDC: How to use

Once you [set up your OIDC integration](#oidc-setup), the tagtog login page (`/-login`), shows an extra option: {{ page.openid_login_btn }}. Moreover, when a non-logged-yet user goes to a tagtog page that requires authentication, the user will be always redirected to the tagtog login page.

<div class="img-with-caption">
  <img src="/assets/img/sysadmin/oidc-login.png" width="80%" alt="Screenshot: Login with OpenID Connect" />
  <p>tagtog login box when OpenID Connect is enabled on your tagtog OnPremises instance.</p>
</div>

When the user clicks on {{ page.openid_login_btn }}, [the user will be redirected to the authentication mechanism of your OIDC Provider](#oidc-redirect-login-url). Upon a successful authentication, the user's data is sent back to tagtog. Two things can then happen:

* a) If the user's email is already associated to a tagtog user, the login is completed, and the user is redirected to the default page after login.

* b) If the user's email is not yet associated to any tagtog user, but the `usersThatCanBeCreatedAutomaticallyIfNotFoundInTagtog` setting allows it, tagtog creates automatically a user account on tagtog. Then the login is completed, the user can access tagtog, and is redirected to the default page. Note that such users created automatically have no associated password, and therefore (unless you later set a password), cannot login on tagtog with basic authentication.

Upon a successful login, a new tagtog user session begins, and everything else is the same and transparent to the user.

Of course, if the login is not successful on the end of the OIDC Provider, or if the user does not exist yet on tagtog and cannot be created automatically, tagtog will not allow any access and will throw a "Forbidden" error.

Finally, if the user logs out on tagtog, the user session ends with respect to tagtog. Note that tagtog does not log out the user with respect to the external OIDC Provider.


##### OIDC: Redirect Login URL

If you want to skip the tagtog login page, you can also just call the (tagtog) endpoint:

(GET) `{{page.openid_login_url}}`

tagtog will immediately redirect to your OIDC Provider. Everything else will work the same.


</div>


<div class="two-third-col">
  <h3>Auth Tokens</h3>
  <p markdown="1">An alternative SSO system on tagtog is based on **authentication tokens**. These can only be generated by the sysadmin (via API). The sysadmin can then have injected, in a simple reverse proxy server or just simple URL redirections, the corresponding authentication token that distinctively grant one user to login. The sysadmin can keep an internal map of reusable tokens or generate them on-demand programmatically any time a login access is required (see below the `useOnce` API parameter). All auth tokens can easily be deleted at any time (see above: [Revoke all auth tokens](#user-management)).</p>

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

Example: `{{ page.onpremises_tagtog_domain }}/?redirectTo=???&token=bbfd-33878148-6062-4934-a507-af4962753c8f`
</div>

<div class="two-third-col" markdown="1">

#### Revoke auth tokens

Remove all existing token-based logins and registration links. If you think your system's security might have been compromised, you can revoke all auth tokens thus invalidating old token-based logins and registration invitations.
</div>




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
