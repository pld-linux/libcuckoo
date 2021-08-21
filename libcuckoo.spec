# TODO: package libcuckoo-gdb-printers
Summary:	High-performance, compact hash table
Summary(pl.UTF-8):	Wydajna, zwarta tablica asocjacyjna
Name:		libcuckoo
Version:	0.3
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/efficient/libcuckoo/releases
Source0:	https://github.com/efficient/libcuckoo/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	13f68f7d20c8b9d819d6f1b12a3b1dc4
URL:		https://github.com/efficient/libcuckoo
BuildRequires:	cmake >= 3.1.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcuckoo provides a high-performance, compact hash table that allows
multiple concurrent reader and writer threads.

%description -l pl.UTF-8
libcuckoo dostarcza wydajną, zwartą tablicę asocjacyjną, pozwalającą
na wiele wątków czytających i piszących.

%package devel
Summary:	High-performance, compact hash table
Summary(pl.UTF-8):	Wydajna, zwarta tablica asocjacyjna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libcuckoo provides a high-performance, compact hash table that allows
multiple concurrent reader and writer threads.

%description devel -l pl.UTF-8
libcuckoo dostarcza wydajną, zwartą tablicę asocjacyjną, pozwalającą
na wiele wątków czytających i piszących.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/libcuckoo
%{_includedir}/libcuckoo-c
%{_datadir}/cmake/libcuckoo
%{_examplesdir}/%{name}-%{version}
