%define _empty_manifest_terminate_build 0

%define libname %mklibname freeaptx %{major}
%define develname %mklibname freeaptx -d
%define oname freeaptx

%define major 0

Name: libfreeaptx
Version: 0.2.2
Release: 1
Summary: Free (open source) implementation of Audio Processing Technology codec (aptX) forked from libopenaptx 0.2.0.
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/iamthehorker/libfreeaptx
Source0: https://github.com/iamthehorker/libfreeaptx/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

%package -n %{oname}
Summary:       Library for Open Source implementation of aptX codec
Group:         System/Libraries

%description -n %{oname}
This package is a fork of libopenaptx. This library is Open Source implementation library of Audio Processing Technology codec
(aptX) derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This
codec is mainly used in Bluetooth A2DP profile.

%description
this package is a fork of libopenaptx. This is Open Source implementation of Audio Processing Technology codec
(aptX) derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This
codec is mainly used in Bluetooth A2DP profile.

%package -n %{libname}
Summary:       Library for Open Source implementation of aptX codec
Group:         System/Libraries

%description -n %{libname}
This package is a fork of libopenaptx. This is Open Source implementation library of Audio Processing Technology codec
(aptX) derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This
codec is mainly used in Bluetooth A2DP profile.

%package -n %{develname}
Summary: aptX header files
Group: Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package provides files needed to develop programms which use %name.

%prep
%autosetup -p1
# don't strip binaries
sed -i '/^LDFLAGS = -s/d' Makefile

%build
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%endif
%make_build

%install
%make_install PREFIX=%_prefix LIBDIR=%_lib

%files -n %{oname}
%{_bindir}/freeaptxdec
%{_bindir}/freeaptxenc

%files -n %{libname}
%{_libdir}/libfreeaptx.so.%{major}
%{_libdir}/libfreeaptx.so.%{version}
%doc README

%files -n %{develname}
%{_includedir}/freeaptx.h
%{_libdir}/libfreeaptx.so
%{_libdir}/pkgconfig/libfreeaptx.pc

%exclude %_libdir/%name.a
