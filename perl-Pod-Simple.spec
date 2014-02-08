%define	upstream_name	 Pod-Simple
%define upstream_version 3.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl module to parse Pod
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Pod::Escapes)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
Pod::Simple is a module suite for parsing Pod.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/Pod
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.180.0-3mdv2012.0
+ Revision: 765600
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.180.0-2
+ Revision: 764128
- rebuilt for perl-5.14.x

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.180.0-1
+ Revision: 690309
- update to new version 3.18

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.160.0-2
+ Revision: 667297
- mass rebuild

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.160.0-1
+ Revision: 646340
- update to new version 3.16

* Sat Nov 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.150.0-1mdv2011.0
+ Revision: 597204
- update to 3.15

* Tue Jul 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.140.0-2mdv2011.0
+ Revision: 561929
- rebuild

* Mon Jul 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.140.0-1mdv2011.0
+ Revision: 551225
- update to 3.14

* Mon Dec 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.130.0-1mdv2010.1
+ Revision: 480712
- update to 3.13

* Sat Dec 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.110.0-1mdv2010.1
+ Revision: 477729
- update to 3.11

* Fri Nov 13 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.100.0-1mdv2010.1
+ Revision: 465709
- update to 3.10

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.90.0-1mdv2010.1
+ Revision: 461348
- update to 3.09

* Tue Aug 25 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.80.0-2mdv2010.0
+ Revision: 420982
- rebuild

* Fri Jul 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.80.0-1mdv2010.0
+ Revision: 396843
- update to 3.08
- using %%perl_convert_version
- fixed license field

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 3.07-2mdv2009.0
+ Revision: 265432
- rebuild early 2009.0 package (before pixel changes)

* Sat Jun 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.07-1mdv2009.0
+ Revision: 216575
- new version

* Wed Jun 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.06-1mdv2009.0
+ Revision: 215071
- new version

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.05-2mdv2008.1
+ Revision: 180536
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.05-1mdv2007.0
+ Revision: 133692
- new version
- Import perl-Pod-Simple

* Tue Apr 04 2006 Buchan Milne <bgmilne@mandriva.org> 3.04-2mdk
- Rebuild

* Mon Jan 23 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.04-1mdk
- New release 3.04
- use mkrel

* Tue Nov 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.03-1mdk
- 3.03
- Fix URL (maintainer change)

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 3.02-5mdk
- fix deps

* Wed Jun 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.02-4mdk 
- better url
- drop useless empty directories
- spec cleanup
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.02-3mdk 
- removed MANIFEST
- added mising doc files

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.02-2mdk
- fix buildrequires in a backward compatible way

* Fri Jun 11 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 3.02-1mdk
- 3.02
- cosmetics

* Wed May 12 2004 Michael Scherer <misc@mandrake.org> 2.06-1mdk
- New release 2.06

* Tue Apr 06 2004 Michael Scherer <misc@mandrake.org> 2.05-2mdk
- fix upload

* Tue Mar 16 2004 Michael Scherer <misc@mandrake.org> 2.05-1mdk
- First MandrakeSoft Package

