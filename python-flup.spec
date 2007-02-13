%define		_release	r1849
Summary:	Random collection of WSGI modules
Summary(pl.UTF-8):	Zestaw różnych modułów WSGI
Name:		python-flup
Version:	0.5
Release:	0.%{_release}.1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://www.saddi.com/software/flup/dist/flup-%{_release}.tar.gz 
# Source0-md5:	77896ee4f4dbd56d2663c12cec2a9689
URL:		http://www.saddi.com/software/flup/
BuildRequires:	python-devel
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
%setup -q -n flup-%{_release}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{py_sitescriptdir}/flup*
