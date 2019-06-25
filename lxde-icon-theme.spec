Summary:	LXDE icon theme
Name:		lxde-icon-theme
Version:	0.5.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		http://www.lxde.org
Source0:	https://sourceforge.net/projects/lxde/files/LXDE%20Icon%20Theme/lxde-icon-theme-%{version}/%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
This package contains nuoveXT2 icon theme for LXDE.

%prep
%setup -q
find -name .gitignore -delete

%build
%configure

%install
%makeinstall_std

%files
%dir %{_iconsdir}/nuoveXT2
%dir %{_iconsdir}/nuoveXT2/??*x*
%dir %{_iconsdir}/nuoveXT2/??*x*/*
%{_iconsdir}/nuoveXT2/??*x*/*/*
%dir %{_iconsdir}/nuoveXT2/extra
%{_iconsdir}/nuoveXT2/extra/*.png
%{_iconsdir}/nuoveXT2/index.theme
%ghost %{_iconsdir}/nuoveXT2/icon-theme.cache
