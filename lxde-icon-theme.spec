Summary:	LXDE icon theme
Name:		lxde-icon-theme
Version:	0.5.0
Release:	10
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		http://www.lxde.org
Source0:	http://freefr.dl.sourceforge.net/project/lxde/LXDE%20Icon%20Theme/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildArch:	noarch
%rename		nuoveXT2-icon-theme

%description
This package contains nuoveXT2 icon theme for LXDE.

%prep
%setup -q
find -name .gitignore -delete

%build
%configure2_5x

%install
%makeinstall_std

touch %{buildroot}%{_iconsdir}/nuoveXT2/icon-theme.cache

%post
%update_icon_cache nuoveXT2

%postun
%clean_icon_cache nuoveXT2

%files
%dir %{_iconsdir}/nuoveXT2
%dir %{_iconsdir}/nuoveXT2/??*x*
%dir %{_iconsdir}/nuoveXT2/??*x*/*
%{_iconsdir}/nuoveXT2/??*x*/*/*
%dir %{_iconsdir}/nuoveXT2/extra
%{_iconsdir}/nuoveXT2/extra/*.png
#%{_iconsdir}/nuoveXT2/index.theme
%ghost %{_iconsdir}/nuoveXT2/icon-theme.cache


%changelog
* Wed Oct 24 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5.0-1
+ Revision: 819662
- cosmetics
- new version
- cleanups

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-3
+ Revision: 666111
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-2mdv2011.0
+ Revision: 606441
- rebuild

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 0.0.1-1mdv2010.1
+ Revision: 476249
- import lxde-icon-theme


