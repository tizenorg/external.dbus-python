# 
# 

Name:       dbus-python
Summary:    D-Bus Python Bindings
Version:    0.83.1
Release:    2
Group:      System/Libraries
License:    MIT
URL:        http://www.freedesktop.org/software/dbus/
Source0:    http://dbus.freedesktop.org/releases/dbus-python/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(dbus-1) >= 0.90
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.70
BuildRequires:  python-devel

%description
D-Bus python bindings for use with python programs.


%package devel
Summary:    Libraries and headers for dbus-python
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %name = %{version}-%{release}

%description devel
Headers and static libraries for hooking up custom mainloops to the dbus python
bindings.



%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}
%make_install



#PKG_CONFIG_PATH=%{_libdir}/pkgconfig %{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT









%files
%defattr(-,root,root,-)
%doc COPYING README
%exclude %{_datadir}/doc/dbus-python
%dir %{python_sitelib}/dbus
%dir %{python_sitelib}/dbus/mainloop
%{python_sitearch}/*.so
%{python_sitelib}/*.py*
%{python_sitelib}/dbus/*.py*
%{python_sitelib}/dbus/mainloop/*.py*
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
%doc ChangeLog NEWS TODO
%doc doc/API_CHANGES.txt doc/HACKING.txt doc/tutorial.txt
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

