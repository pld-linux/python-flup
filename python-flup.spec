%define		_realname	flup
Summary:	Random collection of WSGI modules
Summary(pl.UTF-8):	Zestaw różnych modułów WSGI
Name:		python-%{_realname}
Version:	1.0.2
Release:	2
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://www.saddi.com/software/flup/dist/%{_realname}-%{version}.tar.gz 
# Source0-md5:	24dad7edc5ada31dddd49456ee8d5254
URL:		http://www.saddi.com/software/flup/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%pyrequires_eq  python-modules
Requires:	python-elementtree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Python package is a random collection of WSGI modules.

%description -l pl.UTF-8
Ten pakiet Pythona jest zestawem różnych modułów WSGI

%prep
%setup -q -n %{_realname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{py_sitescriptdir}/flup*
