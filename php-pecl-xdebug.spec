%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)
%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")
%define beta RC2

Name:           php-pecl-xdebug
Version:        2.0.0
Release:        0.3.%{beta}%{?dist}
Summary:        PECL package for debugging PHP scripts

License:        PHP License
Group:          Development/Languages
URL:            http://pecl.php.net/package/xdebug
Source0:        http://pecl.php.net/get/xdebug-%{version}%{beta}.tgz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  php-devel
Requires:       php-api = %{php_apiver}
Provides:       php-pecl(Xdebug) = %{version}-%{release}

%description
The Xdebug extension helps you debugging your script by providing a lot
of valuable debug information.


%prep
%setup -q -n xdebug-%{version}%{beta}


%build
phpize
%configure --enable-xdebug
make


%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/php.d
cat > %{buildroot}%{_sysconfdir}/php.d/xdebug.ini << 'EOF'
; Enable xdebug extension module
zend_extension=%{php_extdir}/xdebug.so
EOF


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changelog CREDITS LICENSE NEWS README
%config(noreplace) %{_sysconfdir}/php.d/xdebug.ini
%{php_extdir}/xdebug.so


%changelog
* Mon Jan 15 2007 Christopher Stone <chris.stone@gmail.com> 2.0.0-0.3.RC2
- Upstream sync

* Sun Oct 29 2006 Christopher Stone <chris.stone@gmail.com> 2.0.0-0.2.RC1
- Upstream sync

* Wed Sep 06 2006 Christopher Stone <chris.stone@gmail.com> 2.0.0-0.1.beta6
- Remove Provides php-xdebug
- Fix Release
- Remove prior changelog due to Release number change
