%define debug_package %nil
%define snap %nil

Summary:	Material Design implemented in QtQuick
Name:		qml-material
Version:	0.2.0
Release:	1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/qml-material
# git clone https://github.com/papyros/qml-material.git
# git archive --format=tar --prefix qml-material-0.0.6-$(date +%Y%m%d)/ HEAD | xz -vf > qml-material-0.0.6-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Declarative)
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtquickcontrols
Requires:	qt5-qtquickcontrols
Requires:	qt5-qtgraphicaleffects
Requires:	qt5-qttools

%description
This is a library of QML widgets implementing
Google's Material Design.

%prep
%setup -q

%build
%qmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
rm -rf %{_buildroot}%{_qt5_libdir}/qt5/tests/tst_material/tst_material

%files
%dir %{_qt5_libdir}/qt5/qml/Material
%dir %{_qt5_libdir}/qt5/qml/QtQuick/Controls/Styles/Material
%{_qt5_libdir}/qt5/qml/Material/*
%{_qt5_libdir}/qt5/tests/tst_material/tst_material
%{_qt5_libdir}/qt5/qml/QtQuick/Controls/Styles/Material/*.qml
%{_qt5_libdir}/qt5/qml/QtQuick/Controls/Styles/Material/qmldir
