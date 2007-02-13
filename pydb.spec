Summary:	Pydb - Extended Python Debugger
Summary(pl.UTF-8):	Pydb - rozszerzony debugger Pythona
Name:		pydb
Version:	1.18
Release:	1
License:	GPL v2
Group:		Development/Languages/Python	
Source0:	http://dl.sourceforge.net/bashdb/%{name}-%{version}.tar.gz
# Source0-md5:	585b84edff47b826f8b12f72f09230ad
Source1:	%{name}-doc-1.15.tar.gz
# Source1-md5:	7132f73ec63534215004fa08bee3b813
Patch0:		%{name}-install.patch
URL:		http://bashdb.sourceforge.net/pydb/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	emacs >= 21
BuildRequires:	python >= 2.1
BuildRequires:	rpmbuild(macros) >= 1.231
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An enhanced Python command-line debugger Pydb is a command-line
debugger for Python. It is based on the standard Python debugger pdb,
but has a number of added features. Particularly, it is suitable for
use with DDD, a graphical debugger front end.

%description -l pl.UTF-8
Ulepszony debugger Pythona działający z linii poleceń. Jest oparty na
pdb - standardowym debuggerze Pythona, ale ma wiele dodatkowych
możliwości. W szczególności nadaje się do używania z DDD - graficznym
interfejsem debuggera.

%package -n emacs-pydb
Summary:	Pydb support for Emacs
Summary(pl.UTF-8):	Obsługa Pydb dla Emacsa
Group:		Development/Languages/Python
Requires:	pydb = %{version}-%{release}
Requires:	emacs >= 21

%description -n emacs-pydb
Pydb support for Emacs.

%description -n emacs-pydb -l pl.UTF-8
Obsługa Pydb dla Emacsa.

%prep
%setup -q -b1
%patch0 -p1 

%build
%{__autoconf}
%{__automake}
%configure \
	--with-site-packages="%{py_sitescriptdir}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS Doc/lib
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/pydb.doc
%attr(755,root,root) %{py_sitescriptdir}/%{name}/pydb.py
%{_mandir}/man1/*

%files -n emacs-pydb
%defattr(644,root,root,755)
%doc emacs/{pydb.el,python-mode.el.diff}
%{_emacs_lispdir}/*.elc
