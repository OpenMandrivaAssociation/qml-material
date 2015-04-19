%define debug_package %nil
%define snap	20150419

Summary:	Material Design implemented in QtQuick
Name:		qml-material
Version:	0.0.6
Release:	1.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/qml-material
# git clone https://github.com/papyros/qml-material.git
# git archive --format=tar --prefix qml-material-0.0.6-$(date +%Y%m%d)/ HEAD | xz -vf > qml-material-0.0.6-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Qml)

%description
This is a library of QML widgets implementing
Google's Material Design.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
%qmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
rm -rf %{_buildroot}%{_qt5_libdir}/qt5/tests/tst_material/tst_material

%files
%dir %{_qt5_libdir}/qt5/qml/Material
%{_qt5_libdir}/qt5/qml/Material/*
%{_qt5_libdir}//qt5/tests/tst_material/tst_material
