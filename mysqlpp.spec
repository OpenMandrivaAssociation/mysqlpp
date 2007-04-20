%define major           2
%define libname_orig    %mklibname %{name}
%define libname         %{libname_orig}%{major}

Name:           mysqlpp
Version:        2.2.3
Release:        %mkrel 1
Epoch:          0
Summary:        C++ wrapper for MySQL's C API
License:        LGPL
Group:          Development/Databases
URL:            http://tangentsoft.net/mysql++/
Source0:        http://tangentsoft.net/mysql++/releases/mysql++-%{version}.tar.gz
BuildRequires:  MySQL-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
MySQL++ is a C++ wrapper for MySQL's C API. It is built around STL 
principles, to make dealing with the database as easy as dealing with an 
STL container.

%package -n %{libname}
Summary:        C++ wrapper for MySQL's C API
Group:          System/Libraries
Provides:       %{libname_orig}

%description -n %{libname}
MySQL++ is a C++ wrapper for MySQL's C API. It is built around STL 
principles, to make dealing with the database as easy as dealing with an 
STL container.

%package -n %{libname}-devel
Summary:        Development files for MySQL++
Group:          Development/Databases
Provides:       %{libname_orig}-devel
Provides:       lib%{name}-devel
Requires:       %{libname} = %{epoch}:%{version}-%{release}

%description -n %{libname}-devel
This package contains static libraries and headers of MySQL++ which are
useful when you develop or compile any applications/libraries using
MySQL C++ interface.

%prep
%setup -q -n mysql++-%{version}
%{_bindir}/find . -type d -name CVS | %{_bindir}/xargs -t %{__rm} -rf

%build
%{configure2_5x} --with-mysql-lib=%{_libdir} \
                 --enable-static \
                 --enable-thread-check
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall}

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(0644,root,root,0755)
%doc COPYING CREDITS ChangeLog HACKERS LICENSE README.* Wishlist
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(0644,root,root,0755)
%doc doc examples/*.{cpp,h}
%defattr(-,root,root)
%{_includedir}/mysql++
%{_libdir}/lib*.so
