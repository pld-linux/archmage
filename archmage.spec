%include        /usr/lib/rpm/macros.python

Summary:	CHM (Compiled HTML) Decompressor
Summary(pl):	Dekompresor plików CHM (Compiled HTML)
Name:		archmage
Version:	0.0.6
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/sourceforge/archmage/%{name}-%{version}.tar.gz
# Source0-md5:	0ab0e7c51fbf10be0a2719f5b5f329f8
URL:		http://archmage.sf.net/
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arCHMage is an extensible reader and decompiler for files in the CHM
format. This is the format used by Microsoft HTML help, and is also
known as Compiled HTML. arCHMage is based on chmlib by Jed Wing.

%description -l pl
arCHMage jest rozszerzalnym czytnikiem i dekompilatorem dla plików w
formacie CHM. Jest to format u¿ywany przez pliki pomocy Microsoft
HTML, zwane tak¿e jako skompilowany HTML. arCHMage bazuje na chmlib
Jediego Winga.

%prep
%setup -q

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
%doc doc/* README
