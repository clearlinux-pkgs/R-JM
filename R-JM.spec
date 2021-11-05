#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-JM
Version  : 1.4.8
Release  : 26
URL      : https://cran.r-project.org/src/contrib/JM_1.4-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/JM_1.4-8.tar.gz
Summary  : Joint Modeling of Longitudinal and Survival Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-xtable
BuildRequires : R-xtable
BuildRequires : buildreq-R

%description
JM: Joint Models for Longitudinal and Survival Data using Maximum Likelihood
================
[![Travis-CI Build Status](https://travis-ci.org/drizopoulos/JM.svg?branch=master)](https://travis-ci.org/drizopoulos/JM) [![CRAN status](http://www.r-pkg.org/badges/version/JM)](https://cran.r-project.org/package=JM) [![](https://cranlogs.r-pkg.org/badges/grand-total/JM)](https://CRAN.R-project.org/package=JM) [![Download counter](http://cranlogs.r-pkg.org/badges/JM)](https://cran.r-project.org/package=JM)
[![Research software impact](http://depsy.org/api/package/cran/JM/badge.svg)](http://depsy.org/package/r/JM)

%prep
%setup -q -c -n JM
cd %{_builddir}/JM

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589520949

%install
export SOURCE_DATE_EPOCH=1589520949
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library JM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library JM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library JM
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc JM || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/JM/CITATION
/usr/lib64/R/library/JM/DESCRIPTION
/usr/lib64/R/library/JM/INDEX
/usr/lib64/R/library/JM/Meta/Rd.rds
/usr/lib64/R/library/JM/Meta/data.rds
/usr/lib64/R/library/JM/Meta/features.rds
/usr/lib64/R/library/JM/Meta/hsearch.rds
/usr/lib64/R/library/JM/Meta/links.rds
/usr/lib64/R/library/JM/Meta/nsInfo.rds
/usr/lib64/R/library/JM/Meta/package.rds
/usr/lib64/R/library/JM/NAMESPACE
/usr/lib64/R/library/JM/NEWS
/usr/lib64/R/library/JM/R/JM
/usr/lib64/R/library/JM/R/JM.rdb
/usr/lib64/R/library/JM/R/JM.rdx
/usr/lib64/R/library/JM/data/Rdata.rdb
/usr/lib64/R/library/JM/data/Rdata.rds
/usr/lib64/R/library/JM/data/Rdata.rdx
/usr/lib64/R/library/JM/help/AnIndex
/usr/lib64/R/library/JM/help/JM.rdb
/usr/lib64/R/library/JM/help/JM.rdx
/usr/lib64/R/library/JM/help/aliases.rds
/usr/lib64/R/library/JM/help/paths.rds
/usr/lib64/R/library/JM/html/00Index.html
/usr/lib64/R/library/JM/html/R.css
