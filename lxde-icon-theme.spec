# git snapshot
#global snapshot 1
%if 0%{?snapshot}
	%global commit		a1ceb9979f8f55cf48dc59a161c77162b968a915
	%global commitdate	20140910
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	LXDE icon theme
Name:		lxde-icon-theme
Version:	0.5.2
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://www.lxde.org
#Source0:	https://sourceforge.net/projects/lxde/files/LXDE%20Icon%20Theme/lxde-icon-theme-%{version}/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/%{name}/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz

BuildArch:	noarch

%description
This package contains nuoveXT2 icon theme for LXDE.

%files
%dir %{_iconsdir}/nuoveXT2
%dir %{_iconsdir}/nuoveXT2/??*x*
%dir %{_iconsdir}/nuoveXT2/??*x*/*
%{_iconsdir}/nuoveXT2/??*x*/*/*
%dir %{_iconsdir}/nuoveXT2/extra
%{_iconsdir}/nuoveXT2/extra/*.png
%{_iconsdir}/nuoveXT2/index.theme
%ghost %{_iconsdir}/nuoveXT2/icon-theme.cache

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

