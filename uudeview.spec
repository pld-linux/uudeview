Summary:	Smart decoder for uuencode, xxencode, Base64 and BinHex
Summary(pl):	Uniwersalny dekoder uuencode, xxencode, Base64 i BinHex
Name:		uudeview
Version:	0.5.13
Release:	2
License:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source:		http://www.informatik.uni-frankfurt.de/~fp/uudeview/Apps/frank/%{name}-%{version}.tar.gz
URL:		http://www.uni-frankfurt.de/~fp/uudeview/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UUDeview is a smart decoder for several surfaces which are common in email
and Usenet. It can decode uuencode, xxencode, Base64 and BinHex. It can
handle multiple files and multiple parts, even in random order. Also an
encoder is attached, UUEnview.

%description -l pl
UUDeview jest przydatnym narzêdziem do dekodowania popularnych formatów,
takich jak uuencode, xxencode, Base64 i BinHex. Potrafi poradziæ sobie z
wieloma plikami w wielu czê¶ciach, nawet wymieszanych. W pakiecie znajduje
siê tak¿e program do kodowania plików na wy¿ej wymienione formaty (oprócz
BinHex).

%prep
%setup -q

%build
%configure \
	--without-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

gzip -9nf HISTORY HOWTO IAFA-PACKAGE 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
