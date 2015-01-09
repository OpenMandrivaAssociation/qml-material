%define debug_package %nil
%define snap 20150109

Summary:	Quantum desktop shell
Name:		qml-material
Version:	0.0.0
Release:	0.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/quantum-os/qml-material
# git archive --format=tar --prefix=qml-material-0.0.0-20150109/ HEAD | xz -vf > qml-material-0.0.0-20150109.tar.xz
Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel

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

%files
