%define	module	Pod-Simple
%define	name	perl-%{module}
%define version 3.06
%define release %mkrel 1

Summary:	Perl module to parse Pod
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildRequires:	perl(Pod::Escapes)
BuildRequires:	perl(HTML::Entities)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Pod::Simple is a module suite for parsing Pod.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Pod
%{perl_vendorlib}/*.pod
%{_mandir}/man3/*


