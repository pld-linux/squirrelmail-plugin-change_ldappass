%define		_plugin	change_ldappass
%define		_plugin_version 2.0
%define		_squirrel_version_required 1.4.0
%define		_version_rpm %{_plugin_version}_%{_squirrel_version_required}
%define		_version_tgz %{_plugin_version}-%{_squirrel_version_required}
Summary:	A squirrel interface to change passwords
Summary(pl.UTF-8):	Wiewiórczy interfejs do zmiany haseł
Name:		squirrelmail-plugin-%{_plugin}
Version:	%{_plugin_version}_%{_squirrel_version_required}
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{_version_tgz}.tar.gz
# Source0-md5:	336c266b5194c3cb274a9c37b62ee335
URL:		http://www.squirrelmail.org/plugin_view.php?id=26
Requires:	squirrelmail >= 1.4.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_squirreldir	%{_datadir}/squirrelmail
%define		_squirreldata	/var/lib/squirrelmail
%define		_plugindir	%{_squirreldir}/plugins/%{_plugin}

%description
This is a Squirrelmail plugin to change a users password which is
stored in an LDAP database (in a posixAccount objectClass) and
optionally to synchronise the password change in samba's smbpasswd
(encrypted password) file.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zmiany haseł użytkowników trzymanych w
bazie LDAP (dla objectClass posixAccount) i opcjonalnie
synchronizowania zmian w pliku smbpasswd z pakietu samba.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

cp -R *.php* locale $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_plugindir}
