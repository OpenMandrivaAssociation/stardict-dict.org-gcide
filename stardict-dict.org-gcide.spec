%define	version	2.4.2
%define rel	4
%define release	%mkrel %rel
%define dict_format_version	2.4.2

Summary:	GCIDE english dictionray for StarDict 2
Name:		stardict-dict.org-gcide
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
URL:		https://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-dictd_www.dict.org_gcide-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
GCIDE (GNU Collaborative International Dictionary of English) converted into
StarDict 2 format (originally for dictd)

%prep
%setup -q -n stardict-dictd_www.dict.org_gcide-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 *.ifo *.idx* *.dict.dz $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*



%changelog
* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.4.2-4mdv2009.0
+ Revision: 140851
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-4mdv2008.1
+ Revision: 127632
- kill re-definition of %%buildroot on Pixel's request


* Wed Nov 23 2005 Eskild Hustvedt <eskild@mandriva.org> 2.4.2-4mdk
- Include *.ifo file
- %%mkrel

* Sat Oct 01 2005 Abel Cheung <deaddog@mandriva.org> 2.4.2-3mdk
- Rebuild

* Tue Jun 01 2004 Abel Cheung <deaddog@deaddog.org> 2.4.2-2mdk
- Dictionaries require main program as well

* Fri Nov 28 2003 Abel Cheung <deaddog@deaddog.org> 2.4.2-1mdk
- New version
- Conflict with old version of stardict

* Mon Jul 28 2003 Abel Cheung <maddog@linux.org.hk> 2.1.0-1mdk
- First Mandrake style spec

