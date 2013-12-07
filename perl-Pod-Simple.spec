%define	modname	Pod-Simple
%define modver	3.18

Summary:	Perl module to parse Pod
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Pod/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Pod::Escapes)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl-devel

%description
Pod::Simple is a module suite for parsing Pod.

%prep
%setup -qn %{modname}-%{modver}

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

