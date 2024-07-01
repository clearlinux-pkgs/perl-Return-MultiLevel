#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Return-MultiLevel
Version  : 0.08
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Return-MultiLevel-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Return-MultiLevel-0.08.tar.gz
Source1  : https://mirrors.kernel.org/debian/pool/main/libr/libreturn-multilevel-perl/libreturn-multilevel-perl_0.05-1.debian.tar.xz
Summary  : 'Return across multiple call levels'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Return-MultiLevel-license = %{version}-%{release}
Requires: perl-Return-MultiLevel-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
NAME
Return::MultiLevel - Return across multiple call levels
VERSION
version 0.08

%package dev
Summary: dev components for the perl-Return-MultiLevel package.
Group: Development
Provides: perl-Return-MultiLevel-devel = %{version}-%{release}
Requires: perl-Return-MultiLevel = %{version}-%{release}

%description dev
dev components for the perl-Return-MultiLevel package.


%package license
Summary: license components for the perl-Return-MultiLevel package.
Group: Default

%description license
license components for the perl-Return-MultiLevel package.


%package perl
Summary: perl components for the perl-Return-MultiLevel package.
Group: Default
Requires: perl-Return-MultiLevel = %{version}-%{release}

%description perl
perl components for the perl-Return-MultiLevel package.


%prep
%setup -q -n Return-MultiLevel-0.08
cd %{_builddir}
tar xf %{_sourcedir}/libreturn-multilevel-perl_0.05-1.debian.tar.xz
cd %{_builddir}/Return-MultiLevel-0.08
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Return-MultiLevel-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Return-MultiLevel
cp %{_builddir}/Return-MultiLevel-0.08/LICENSE %{buildroot}/usr/share/package-licenses/perl-Return-MultiLevel/0ab9a6cc84763ec21b994b34170b2eb0ccae31e9
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Return-MultiLevel/b2c2c7c0712e90307a37bf9c3da33f070e00938a
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Return::MultiLevel.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Return-MultiLevel/0ab9a6cc84763ec21b994b34170b2eb0ccae31e9
/usr/share/package-licenses/perl-Return-MultiLevel/b2c2c7c0712e90307a37bf9c3da33f070e00938a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
