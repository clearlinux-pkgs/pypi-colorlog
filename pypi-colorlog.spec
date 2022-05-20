#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-colorlog
Version  : 6.6.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/8e/8f/1537ebed273d43edd3bb21f1e5861549b7cfcb1d47523d7277cab988cec2/colorlog-6.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/8f/1537ebed273d43edd3bb21f1e5861549b7cfcb1d47523d7277cab988cec2/colorlog-6.6.0.tar.gz
Summary  : Add colours to the output of Python's logging module.
Group    : Development/Tools
License  : MIT
Requires: pypi-colorlog-license = %{version}-%{release}
Requires: pypi-colorlog-python = %{version}-%{release}
Requires: pypi-colorlog-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)

%description
===========================

%package license
Summary: license components for the pypi-colorlog package.
Group: Default

%description license
license components for the pypi-colorlog package.


%package python
Summary: python components for the pypi-colorlog package.
Group: Default
Requires: pypi-colorlog-python3 = %{version}-%{release}

%description python
python components for the pypi-colorlog package.


%package python3
Summary: python3 components for the pypi-colorlog package.
Group: Default
Requires: python3-core
Provides: pypi(colorlog)

%description python3
python3 components for the pypi-colorlog package.


%prep
%setup -q -n colorlog-6.6.0
cd %{_builddir}/colorlog-6.6.0
pushd ..
cp -a colorlog-6.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653010070
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-colorlog
cp %{_builddir}/colorlog-6.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-colorlog/5d70b54581cc4a1ab2ee60f7bea991a2d56340a5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-colorlog/5d70b54581cc4a1ab2ee60f7bea991a2d56340a5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
