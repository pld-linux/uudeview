#
# Conditional build:
%bcond_without  doc	# don't build HTML documentation
%bcond_without  x11	# don't build tk GUI

Summary:	Smart decoder for uuencode, xxencode, Base64 and BinHex
Summary(pl.UTF-8):	Uniwersalny dekoder uuencode, xxencode, Base64 i BinHex
Summary(pt_BR.UTF-8):	UUDeview, decodificador de vários tipos de arquivos
Name:		uudeview
Version:	0.5.20
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://www.fpx.de/fp/Software/UUDeview/download/%{name}-%{version}.tar.gz
# Source0-md5:	0161abaec3658095044601eae82bbc5b
Patch0:		%{name}-shared.patch
URL:		http://www.fpx.de/fp/Software/UUDeview/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%if %{with doc}
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-latex
BuildRequires:	tetex-latex-psnfss
BuildRequires:	tetex-tex-misc
BuildRequires:	transfig
%endif
%if %{with x11}
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UUDeview is a smart decoder for several surfaces which are common in
email and Usenet. It can decode uuencode, xxencode, Base64 and BinHex.
It can handle multiple files and multiple parts, even in random order.
Also an encoder is attached, UUEnview.

%description -l pl.UTF-8
UUDeview jest przydatnym narzędziem do dekodowania popularnych
formatów, takich jak uuencode, xxencode, Base64 i BinHex. Potrafi
poradzić sobie z wieloma plikami w wielu częściach, nawet
wymieszanych. W pakiecie znajduje się także program do kodowania
plików na wyżej wymienione formaty (oprócz BinHex).

%description -l pt_BR.UTF-8
Decodificador UUencode, XXencode, Base64, BinHex, etc. Inclui um
codificador.

%package x11
Summary:	xdeview - uudeview with a GUI
Summary(pl.UTF-8):	xdeview - uudeview z graficznym interfejsem
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description x11
xdeview - uudeview with a GUI.

%description x11 -l pl.UTF-8
xdeview - uudeview z graficznym interfejsem.

%package devel
Summary:	uulib header files
Summary(pl.UTF-8):	Pliki nagłówkowe uulib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
uulib header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe uulib.

%package static
Summary:	uulib static library
Summary(pl.UTF-8):	Statyczna biblioteka uulib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
uulib static library.

%description static -l pl.UTF-8
Statyczna biblioteka uulib.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	%{!?with_x11:--disable-tcl}

%{__make}
%{?with_doc:%{__make} ps -C doc}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%{__make} install -C uulib \
	DESTDIR=$RPM_BUILD_ROOT

mv -f inews/README README.inews

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc HISTORY README*
%attr(755,root,root) %{_libdir}/libuu.so.*.*
%attr(755,root,root) %{_bindir}/minews
%attr(755,root,root) %{_bindir}/uudeview
%attr(755,root,root) %{_bindir}/uuenview
%{_mandir}/man1/uu*

%if %{with x11}
%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uuwish
%attr(755,root,root) %{_bindir}/xdeview
%{_mandir}/man1/xdeview.1*
%endif

%files devel
%defattr(644,root,root,755)
%{?with_doc:%doc doc/library.ps}
%attr(755,root,root) %{_libdir}/libuu.so
%{_libdir}/libuu.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libuu.a
