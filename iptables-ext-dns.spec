%define _unpackaged_files_terminate_build 0
%define _mod_dir kernel/net/netfilter

Summary: Administration tool for IPv4/IPv6 TCP/UDP packet filtering.
Name: iptables-ext-dns
Version: 1.0.3
Release: 0%{?dist}
License: GPLv3
Group: System Environment/Base
Source: https://github.com/mimuret/iptables-ext-dns/iptables-ext-dns-%{version}.zip
URL: https://github.com/mimuret/iptables-ext-dns
Requires: iptables iptables-ipv6 nc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX
BuildRequires: gcc make automake libtool iptables-devel kernel-headers kernel-devel

%description
Administration tool for IPv4/IPv6 TCP/UDP packet filtering.

%prep
%{__rm} -rf ${RPM_BUILD_ROOT}

%setup
autoreconf --install --force --verbose
%{configure} --libdir=/%{_lib}

%build
%{__make}

%install
install -m755 -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}-%{version}/test
install -m755 test/*.sh ${RPM_BUILD_ROOT}%{_datadir}/%{name}-%{version}/test

install -m755 -d ${RPM_BUILD_ROOT}/lib/modules/%(uname -r)/%{_mod_dir}
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=%{_mod_dir}
%{__make} DESTDIR=%{buildroot} install

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%post
/sbin/ldconfig
/sbin/depmod -A

%postun
/sbin/ldconfig
/sbin/depmod -A

%files
%defattr(-,root,root)

%doc LICENSE
%doc README.md

/lib64/xtables/libxt_dns.a
/lib64/xtables/libxt_dns.la
/lib64/xtables/libxt_dns.so
/lib64/xtables/libxt_dns.so.1
/lib64/xtables/libxt_dns.so.%{version}
/lib/modules/%(uname -r)/%{_mod_dir}/xt_dns.ko

%{_datadir}

%changelog
* Mon Feb 29 2016 t0r0t0r0
- 2nd

* Fri Feb 26 2016 t0r0t0r0
- 1st