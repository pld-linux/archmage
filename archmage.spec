Summary:	CHM (Compiled HTML) Decompressor
Summary(pl.UTF-8):	Dekompresor plików CHM (Compiled HTML)
Name:		archmage
Version:	0.0.6
Release:	5
License:	GPL
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/archmage/%{name}-%{version}.tar.gz
# Source0-md5:	0ab0e7c51fbf10be0a2719f5b5f329f8
Patch0:		%{name}-morearchs.patch
URL:		http://archmage.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arCHMage is an extensible reader and decompiler for files in the CHM
format. This is the format used by Microsoft HTML help, and is also
known as Compiled HTML. arCHMage is based on chmlib by Jed Wing.

%description -l pl.UTF-8
arCHMage jest rozszerzalnym czytnikiem i dekompilatorem dla plików w
formacie CHM. Jest to format używany przez pliki pomocy Microsoft
HTML, zwane także jako skompilowany HTML. arCHMage bazuje na chmlib
Jediego Winga.

%prep
%setup -q
%patch0 -p1

%build
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/arch.conf
%attr(755,root,root) %{_bindir}/archmage
%{py_sitedir}/CHM.py[co]
%{py_sitedir}/chmlib.py[co]
%{py_sitedir}/mod_chm.py[co]
%attr(755,root,root) %{py_sitedir}/_chmlib.so
%{_datadir}/archmage
%{py_sitedir}/%{name}-%{version}-py*.egg-info
