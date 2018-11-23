#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Return-MultiLevel
Version  : 0.05
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/MA/MAUKE/Return-MultiLevel-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MAUKE/Return-MultiLevel-0.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/libreturn-multilevel-perl/libreturn-multilevel-perl_0.05-1.debian.tar.xz
Summary  : 'return across multiple call levels'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::Munge)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
NAME
Return::MultiLevel - return across multiple call levels
INSTALLATION
To download and install this module, use your favorite CPAN client, e.g.
"cpan":

%package dev
Summary: dev components for the perl-Return-MultiLevel package.
Group: Development
Provides: perl-Return-MultiLevel-devel = %{version}-%{release}

%description dev
dev components for the perl-Return-MultiLevel package.


%prep
%setup -q -n Return-MultiLevel-0.05
cd ..
%setup -q -T -D -n Return-MultiLevel-0.05 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Return-MultiLevel-0.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Return/MultiLevel.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Return::MultiLevel.3
