%define lib_major 4
%define api 1.0
%define libname %mklibname dee %{api} %{lib_major}
%define gi_name %mklibname dee-gir 1.0
%define libnamedev %mklibname -d dee

Name: dee
Summary: Model to synchronize mutiple instances over DBus
Version: 1.0.10
Release: 1
License: LGPLv2+
Group: System/Libraries
Source0: http://launchpad.net/dee/1.0/%{version}/+download/dee-%{version}.tar.gz
URL: https://launchpad.net/dee
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(glib-2.0) >= 2.26
BuildRequires: pkgconfig(gthread-2.0) >= 2.26
BuildRequires: pkgconfig(gobject-2.0) >= 2.26
BuildRequires: pkgconfig(gio-2.0) >= 2.26
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.26
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools
BuildRequires: vala-devel
BuildRequires: icu-devel

%description
Libdee is a library that uses DBus to provide objects allowing you to create
Model-View-Controller type programs across DBus. It also consists of utility
objects which extend DBus allowing for peer-to-peer discoverability of known
objects without needing a central registrar.

%package -n %{libname}
Summary: Model to synchronize mutiple instances over DBus - Shared lib
Group: System/Libraries

%description -n %{libname}
Libdee is a library that uses DBus to provide objects allowing you to create
Model-View-Controller type programs across DBus. It also consists of utility
objects which extend DBus allowing for peer-to-peer discoverability of known
objects without needing a central registrar.

%package -n %{gi_name}
Summary: GObject Introspection interface library for %{name}
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description -n %{gi_name}
GObject Introspection interface library for %{name}.

%package -n %{libnamedev}
Summary: Libraries and include files for developing with libdee
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
This package contains files that are needed to build applications.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la
# remove python binding because it is not working according to upstream
rm -fr %{buildroot}%py_platsitedir

%files -n %{libname}
%{_libdir}/libdee-%{api}.so.%{lib_major}*

%files -n %{gi_name}
%{_libdir}/girepository-1.0/Dee-1.0.typelib

%files -n %{libnamedev}
%{_bindir}/dee-tool
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/dee-*
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*




%changelog
* Tue May 15 2012 Crispin Boylan <crisb@mandriva.org> 1.0.10-1
+ Revision: 799098
- New release

* Tue Nov 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.5.22-2
+ Revision: 708162
- imported package dee

