#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	GD
%define		pnam	Graph3d
%include	/usr/lib/rpm/macros.perl
Summary:	GD::Graph3d - create 3D graphs with GD and GD::Graph
Summary(pl.UTF-8):	GD::Graph3d - tworzenie grafów trójwymiarowych z pomocą GD i GD::Graph
Name:		perl-GD-Graph3d
Version:	0.63
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f866dcdd1e7e2056bb946ab7ac3fe37b
URL:		http://search.cpan.org/dist/GD-Graph3d/
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-Graph >= 1.30
BuildRequires:	perl-GD-TextUtil
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GD::Graph3d extensions module. It provides 3D graphs for
the GD::Graph module by Martien Verbruggen, which in turn generates
graph using Lincoln Stein's GD.pm.

%description -l pl.UTF-8
To jest moduł GD::Graph3d. Dodaje wykresy 3D do modułu GD::Graph
autorstwa Martiena Verbruggena, który generuje wykresy przy użyciu
modułu GD.pm autorstwa Lincolna Steina.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/GD/Graph3d.pm
%{perl_vendorlib}/GD/Graph/*
%{_mandir}/man3/*
