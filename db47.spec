# based on PLD Linux spec git://git.pld-linux.org/packages/db47.spec
Summary:	Berkeley DB database library for C
Name:		db47
Version:	4.7.25
Release:	6
License:	Sleepycat public license (GPL-like, see LICENSE)
Group:		Libraries
Source0:	http://download.oracle.com/berkeley-db/db-%{version}.tar.gz
# Source0-md5:	ec2b87e833779681a0c3a814aa71359e
Patch0:		http://www.oracle.com/technology/products/berkeley-db/db/update/4.7.25/patch.4.7.25.1
Patch1:		http://www.oracle.com/technology/products/berkeley-db/db/update/4.7.25/patch.4.7.25.2
Patch2:		http://www.oracle.com/technology/products/berkeley-db/db/update/4.7.25/patch.4.7.25.3
Patch3:		http://www.oracle.com/technology/products/berkeley-db/db/update/4.7.25/patch.4.7.25.4
URL:		http://www.oracle.com/technology/products/berkeley-db/db/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	sed
Provides:	db = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB is used by many applications,
including Python and Perl, so this should be installed on all systems.

%package devel
Summary:	Header files for Berkeley database library
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	db-devel
Provides:	db-devel = %{version}-%{release}

%description devel
This package contains the header files, libraries, and documentation
for building programs which use Berkeley DB.

%package cxx
Summary:	Berkeley database library for C++
Group:		Libraries
Obsoletes:	db-cxx
Provides:	db-cxx = %{version}-%{release}

%description cxx
Berkeley database library for C++.

%package cxx-devel
Summary:	Header files for db-cxx library
Group:		Development/Libraries
Requires:	%{name}-cxx = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	db-cxx-devel
Provides:	db-cxx-devel = %{version}-%{release}

%description cxx-devel
Header files for db-cxx library.

%package utils
Summary:	Command line tools for managing Berkeley DB databases
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	db-utils
Provides:	db-utils = %{version}-%{release}

%description utils
This package contains command line tools for managing Berkeley DB
databases.

%prep
%setup -q -n db-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
cp -f /usr/share/automake/config.sub dist

cd build_unix

../dist/%configure \
	--disable-static	\
	--enable-compat185	\
	--enable-cxx		\
	--enable-posixmutexes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}

%{__make} -C build_unix library_install \
	docdir=%{_docdir}/db-%{version}-docs \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB_INSTALL_FILE_LIST=""

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/db-*-docs/{api_tcl,articles,collections,gsg*/JAVA,java,license,porting,ref}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%post	cxx -p /usr/sbin/ldconfig
%postun	cxx -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libdb-4.7.so
%dir %{_docdir}/db-%{version}-docs
%{_docdir}/db-%{version}-docs/index.html

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb-4.so
%attr(755,root,root) %{_libdir}/libdb.so
%{_libdir}/libdb-4.7.la
%{_includedir}/db.h
%{_includedir}/db_185.h

%dir %{_docdir}/db-%{version}-docs/gsg
%dir %{_docdir}/db-%{version}-docs/gsg_db_rep
%dir %{_docdir}/db-%{version}-docs/gsg_txn
%{_docdir}/db-%{version}-docs/api_c
%{_docdir}/db-%{version}-docs/gsg/C
%{_docdir}/db-%{version}-docs/gsg_db_rep/C
%{_docdir}/db-%{version}-docs/gsg_txn/C
%{_docdir}/db-%{version}-docs/images

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_cxx-4.7.so

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_cxx.so
%attr(755,root,root) %{_libdir}/libdb_cxx-4.so
%{_libdir}/libdb_cxx-4.7.la
%{_includedir}/db_cxx.h
%{_docdir}/db-%{version}-docs/api_cxx
%{_docdir}/db-%{version}-docs/gsg/CXX
%{_docdir}/db-%{version}-docs/gsg_db_rep/CXX
%{_docdir}/db-%{version}-docs/gsg_txn/CXX

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/db_archive
%attr(755,root,root) %{_bindir}/db_checkpoint
%attr(755,root,root) %{_bindir}/db_codegen
%attr(755,root,root) %{_bindir}/db_deadlock
%attr(755,root,root) %{_bindir}/db_dump
%attr(755,root,root) %{_bindir}/db_hotbackup
%attr(755,root,root) %{_bindir}/db_load
%attr(755,root,root) %{_bindir}/db_printlog
%attr(755,root,root) %{_bindir}/db_recover
%attr(755,root,root) %{_bindir}/db_stat
%attr(755,root,root) %{_bindir}/db_upgrade
%attr(755,root,root) %{_bindir}/db_verify
%{_docdir}/db-%{version}-docs/utility

