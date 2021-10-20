%define lib_major 4
%define api 1.0
%define libname %mklibname dee %{api} %{lib_major}
%define gi_name %mklibname dee-gir %{api}
%define libnamedev %mklibname -d dee

Name: dee
Summary: Model to synchronize mutiple instances over DBus
Version: 1.2.7
Release: 3
License: LGPLv2+
Group: System/Libraries
Source0: http://launchpad.net/dee/1.0/%{version}/+download/dee-%{version}.tar.gz
Patch0: vapi-skip-properties.patch
Patch1: strict-prototype.patch
Patch2: dee-1.2.7-deprecated-g_type_class_add_private.patch
Patch3: build_no_werror.patch

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
%autopatch -p1
sed -e 's:-Werror::g' -i configure.ac

%build
%configure --disable-static
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la

%files
%doc ChangeLog README TODO COPYING COPYING.GPL
%{_bindir}/dee-tool
%{python_sitearch}/gi/overrides/Dee.*
%{python_sitearch}/gi/overrides/__pycache__/*

%files -n %{libname}
%doc ChangeLog README TODO COPYING COPYING.GPL
%{_libdir}/libdee-%{api}.so.%{lib_major}*

%files -n %{gi_name}
%doc ChangeLog README TODO COPYING COPYING.GPL
%{_libdir}/girepository-1.0/Dee-%{api}.typelib

%files -n %{libnamedev}
%doc ChangeLog README TODO COPYING COPYING.GPL
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/dee-*
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*
