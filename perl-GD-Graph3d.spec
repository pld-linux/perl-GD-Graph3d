%include	/usr/lib/rpm/macros.perl
%define	pdir	GD
%define	pnam	Graph3d
Summary:	GD::Graph3d perl module
Summary(pl):	Modu³ perla GD::Graph3d
Name:		perl-GD-Graph3d
Version:	0.59
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-Graph >= 1.30
BuildRequires:	perl-GD-TextUtil
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GD::Graph3d extensions module. It provides 3D graphs
for the GD::Graph module by Martien Verbruggen, which in turn
generates graph using Lincoln Stein's GD.pm.

%description -l pl
To jest modu³ GD::Graph3d. Dodaje wykresy 3D do modu³u GD::Graph
autorstwa Martiena Verbruggena, który generuje wykresy przy u¿yciu
modu³u GD.pm autorstwa Lincolna Steina.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README test.pl
%{perl_sitelib}/GD/Graph3d.pm
%{perl_sitelib}/GD/Graph/*
%{_mandir}/man3/*
