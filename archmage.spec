Summary:	CHM (Compiled HTML) Decompressor
Summary(pl.UTF-8):	Dekompresor plików CHM (Compiled HTML)
Name:		archmage
Version:	0.4.2.1
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	https://github.com/dottedmag/archmage/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	af3b4393d5d8912ddf93d722725e9b70
URL:		https://github.com/dottedmag/archmage
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
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

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%py3_install

%{__mv} $RPM_BUILD_ROOT%{py3_sitescriptdir}/archmage/arch.conf $RPM_BUILD_ROOT%{_sysconfdir}
ln -sr $RPM_BUILD_ROOT%{_sysconfdir}/arch.conf $RPM_BUILD_ROOT%{py3_sitescriptdir}/archmage/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/arch.conf
%attr(755,root,root) %{_bindir}/archmage
%{py3_sitescriptdir}/archmage
%{py3_sitescriptdir}/%{name}-%{version}-py*.egg-info
