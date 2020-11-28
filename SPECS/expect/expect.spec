Summary:        Expect is a tool for automating interactive applications
Name:           expect
Version:        5.45.4
Release:        4%{?dist}
License:        GPLv2+
URL:            https://sourceforge.net/projects/expect
Source0:        https://sourceforge.net/projects/%{name}/files/Expect/%{version}/%{name}%{version}.tar.gz
%define sha1    expect=a97b2f377c6a799928d6728c2ada55beb7f57d96
Group:          Development/Tools
Vendor:         Microsoft Corporation
Distribution:   Amelia
Requires:       tcl
BuildRequires:  tcl-devel

Patch0:         expect-fix-format-security.patch

%description
Expect is a tool for automating interactive applications such as
telnet, ftp, passwd, fsck, rlogin, tip, etc. Expect is also useful
for testing these same applications.

%package devel
Summary: Headers and development libraries for expect
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: tcl-devel

%description devel
Headers and development libraries for expect

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

%check
make %{?_smp_mflags} test

%files
%defattr(-,root,root)
%license license.terms
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_mandir}/man3/*


%changelog
*   Sun May 31 2020 Henry Beberman <henry.beberman@microsoft.com> - 5.45.4-4
-   Add patch to fix format-security errors. 
*   Sat May 09 00:21:13 PST 2020 Nick Samson <nisamson@microsoft.com> - 5.45.4-3
-   Added %%license line automatically
*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 5.45.4-2
-   Initial CBL-Mariner import from Photon (license: Apache2).
*   Thu Sep 20 2018 Sujay G <gsujay@vmware.com> 5.45.4-1
-   Bump expect version to 5.45.4
*   Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 5.45-3
-   Use standard configure macros
*   Tue Aug 8 2017 Alexey Makhalov <amakhalov@vmware.com> 5.45-2
-   Fix %check section
*   Wed Jul 12 2017 Alexey Makhalov <amakhalov@vmware.com> 5.45-1
-   Initial build. First version
