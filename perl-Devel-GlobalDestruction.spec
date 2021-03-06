#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Devel
%define	pnam	GlobalDestruction
Summary:	Devel::GlobalDestruction - Expose PL_dirty, the flag which marks global destruction
Summary(pl.UTF-8):	Devel::GlobalDestruction - udostępnienie PL_dirty - flagi oznaczającej globalną destrukcję
Name:		perl-Devel-GlobalDestruction
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	24221ba322cf2dc46a1fc99b53e2380b
URL:		http://search.cpan.org/dist/Devel-GlobalDestruction/
BuildRequires:	perl-ExtUtils-CBuilder >= 0.27
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Scope-Guard
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Sub-Exporter-Progressive >= 0.001011
%endif
Requires:	perl-Sub-Exporter-Progressive >= 0.001011
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::GlobalDestruction - expose PL_dirty, the flag which marks
global destruction.

%description -l pl.UTF-8
Devel::GlobalDestruction udostępnia PL_dirty - flagę oznaczającą
globalną destrukcję.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Devel/GlobalDestruction.pm
%{_mandir}/man3/Devel::GlobalDestruction.3pm*
