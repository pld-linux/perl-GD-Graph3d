%include	/usr/lib/rpm/macros.perl
Summary:	GD-Graph3d perl module
Summary(pl):	Modu³ perla GD-Graph3d
Name:		perl-GD-Graph3d
Version:	0.56
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GDGraph3d-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
BuildRequires:	perl-GD-Graph
BuildRequires:	perl-GD-TextUtil
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GD::Graph3d extensions module. It provides 3D graphs
for the GD::Graph module by Martien Verbruggen, which in turn
generates graph using Lincoln Stein's GD.pm.

%description -l pl
To jest modu³ GD::Graph3d. Dodaje wykresy 3D do modu³u GD::Graph
autorstwa Martiena Verbruggena, który generuje wykresy przy u¿yciu
modu³o GD.pm autorstwa Lincolna Steina.

%prep
%setup -q -n GDGraph3d-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz test.pl
%{perl_sitelib}/GD/Graph3d.pm
%{perl_sitelib}/GD/Graph/*
%{_mandir}/man3/*
