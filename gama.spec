Summary:	GNU Gama - adjustment of geodetic networks
Summary(pl.UTF-8):	GNU Gama - wyrównywanie sieci geodezyjnych
Name:		gama
Version:	2.29
Release:	1
License:	GPL v3+
Group:		Applications/Science
Source0:	https://ftp.gnu.org/gnu/gama/%{name}-%{version}.tar.gz
# Source0-md5:	f90c88d7301f8166536ff4396637cfe5
URL:		http://www.gnu.org/software/gama/
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libxml2-progs
BuildRequires:	octave
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	texinfo
BuildRequires:	yaml-cpp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Gama package is dedicated to adjustment of geodetic networks. It
is intended for use with traditional geodetic surveyings which are
still used and needed in special measurements (e.g., underground or
high precision engineering measurements) where the Global Positioning
System (GPS) cannot be used.

%description -l pl.UTF-8
Pakiet GNU Gama służy do wyrównywania sieci geodezyjnych. Jest
przeznaczony do użycia w tradycyjnych badaniach geodezyjnych, które są
nadal używane w specjalnych pomiarach (np. podziemnych lub
precyzyjnych pomiarach inżynierskich), gdzie nie można użyć GPS-a
(Global Positioning System).

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/cmp_xml_file
%attr(755,root,root) %{_bindir}/compare-xyz
%attr(755,root,root) %{_bindir}/gama-g3
%attr(755,root,root) %{_bindir}/gama-local
%attr(755,root,root) %{_bindir}/gama-local-deformation
%attr(755,root,root) %{_bindir}/gama-local-gkf2yaml
%attr(755,root,root) %{_bindir}/gama-local-xml2sql
%attr(755,root,root) %{_bindir}/gama-local-xml2txt
%attr(755,root,root) %{_bindir}/gama-local-yaml2gkf
%attr(755,root,root) %{_bindir}/krumm2gama-local
%{_infodir}/gama.info*
