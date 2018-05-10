sublime-conf
============

My personal configuration for [Sublime Text 3](http://www.sublimetext.com/).

What's inside?
-------------------

* Preferences.
* Keymapping.
* List of installed packages with *Package Control*.

The User Package
-----------------
**Packages/User** is a catch-all directory for custom plugins, snippets, macros, etc.
Consider it your personal area in the packages folder. *Sublime Text 3* will never
overwrite the contents of **Packages/User** during upgrades.


Installation
------------

1. Install **Sublime Text 3**

2. Clone this repo. We're assuming you're going to use your *home* directory.

3. Install [Package Control](http://wbond.net/sublime_packages/package_control).

4. Execute following command (*Linux*):

   ```
   $ ln -s ./User  ~/.config/sublime-text-3/Packages/User
   ```
