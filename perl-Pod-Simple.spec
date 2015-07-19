%define	upstream_name	 Pod-Simple
%define upstream_version 3.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary:    Perl module to parse Pod

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Cwd)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Pod::Escapes) >= 1.40.0
BuildRequires: perl(Symbol)
BuildRequires: perl(Test) >= 1.250.0
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Wrap) >= 98.112.902
BuildRequires: perl(constant)
BuildRequires: perl(integer)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl-devel
BuildArch:  noarch

%description
Pod::Simple is a module suite for parsing Pod.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog META.json META.yml MYMETA.yml README
%{perl_vendorlib}/Pod
%{_mandir}/man3/*

