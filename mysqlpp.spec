%define major           3
%define libname         %mklibname mysqlpp %{major}
%define libname_devel   %mklibname mysqlpp -d

Name:           mysqlpp
Version:        3.0.8
Release:        %mkrel 2
Epoch:          0
Summary:        C++ wrapper for MySQL's C API
License:        LGPLv2+
Group:          Development/Databases
URL:            https://tangentsoft.net/mysql++/
Source0:        http://tangentsoft.net/mysql++/releases/mysql++-%{version}.tar.gz
Patch0:         mysql++-3.0.8-link.patch
BuildRequires:  mysql-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
MySQL++ is a C++ wrapper for MySQL's C API. It is built around STL 
principles, to make dealing with the database as easy as dealing with an 
STL container.

%package -n %{libname}
Summary:        C++ wrapper for MySQL's C API
Group:          System/Libraries

%description -n %{libname}
MySQL++ is a C++ wrapper for MySQL's C API. It is built around STL 
principles, to make dealing with the database as easy as dealing with an 
STL container.

%package -n %{libname_devel}
Summary:        Development files for MySQL++
Group:          Development/Databases
Provides:       mysqlpp-devel = %{epoch}:%{version}-%{release}
Obsoletes:      %{mklibname mysqlpp 2}-devel < %{epoch}:%{version}-%{release}
Requires:       %{libname} = %{epoch}:%{version}-%{release}

%description -n %{libname_devel}
This package contains static libraries and headers of MySQL++ which are
useful when you develop or compile any applications/libraries using
MySQL C++ interface.

%prep
%setup -q -n mysql++-%{version}
%patch0 -p1

perl -pi -e 's/\r$//g;' Changelog *.txt 

%build
%{configure2_5x} --with-mysql-lib=%{_libdir} \
                 --enable-static \
                 --enable-thread-check
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(0644,root,root,0755)
%doc ChangeLog *.txt
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files -n %{libname_devel}
%defattr(0644,root,root,0755)
%doc doc examples/*.{cpp,h}
%defattr(-,root,root)
%{_includedir}/mysql++
%{_libdir}/lib*.so
