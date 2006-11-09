#
# Conditional build:
%bcond_without  doc	# don't build HTML documentation
%bcond_without  x11	# don't build tk GUI

Summary:	Smart decoder for uuencode, xxencode, Base64 and BinHex
Summary(pl):	Uniwersalny dekoder uuencode, xxencode, Base64 i BinHex
Summary(pt_BR):	UUDeview, decodificador de v�rios tipos de arquivos
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

%description -l pl
UUDeview jest przydatnym narz�dziem do dekodowania popularnych
format�w, takich jak uuencode, xxencode, Base64 i BinHex. Potrafi
poradzi� sobie z wieloma plikami w wielu cz�ciach, nawet
wymieszanych. W pakiecie znajduje si� tak�e program do kodowania
plik�w na wy�ej wymienione formaty (opr�cz BinHex).

%description -l pt_BR
Decodificador UUencode, XXencode, Base64, BinHex, etc. Inclui um
codificador.

%package x11
Summary:	xdeview - uudeview with a GUI
Summary(pl):	xdeview - uudeview z graficznym interfejsem
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description x11
xdeview - uudeview with a GUI.

%description x11 -l pl
xdeview - uudeview z graficznym interfejsem.

%package devel
Summary:	uulib header files
Summary(pl):	Pliki nag��wkowe uulib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
uulib header files.

%description devel -l pl
Pliki nag��wkowe uulib.

%package static
Summary:	uulib static library
Summary(pl):	Statyczna biblioteka uulib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
uulib static library.

%description static -l pl
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
