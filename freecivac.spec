#
# TODO: 
#  - fix app name (files are freeciv.mo and so on, so conflicts with freeciv)
# Conditional build:
%define	snapdate 20050502
Summary:	FREE CIVilization clone - AC version
Summary(pl.UTF-8):	Klon FREE CIVilization - wersja AC
Name:		freecivac
Version:	snap.%{snapdate}
Release:	0.1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://vorlon.icpnet.pl/~agaran/%{name}-snap-%{snapdate}.tgz
# Source0-md5:	5dc07e4f5cae347241b42341ea10d83f
Patch0:		%{name}-gtk2-m4.diff
Patch1:		%{name}-slang.diff
URL:		http://freecivac.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# needs to be resolved, mo and /usr/share/freeciv conflict
Conflicts:	freeciv

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Free clone of Sid Meier's Civilization. Free Civilization clone for
Unix and X. This is multiplayer strategic game and you can also play
against computer-AI players.

%description -l pl.UTF-8
Darmowy klon Civilization Sida Meiera, dziaĹajÄcy pod Uniksem i X.
Jest to gra strategiczna dla wielu graczy, moĹźna graÄ takĹźe przeciwko
komputerowej AI.

# yes, i know ugly way, but i wanted to commit what i done @home maybe
# somebody else could fix rest, 
%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
rm configure.in
mv m4/x.252 m4/x.m4
perl -pi -e 's/-lslang-utf8/-lslang/' server/Makefile.am
perl -pi -e 's/-lslang-utf8/-lslang/' client/Makefile.am
chmod +x client/gui-gtk-2.0/rc2c

%build
#%%{__gettextize}
#autoupdate
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	ARFLAGS=rcs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install -d $RPM_BUILD_ROOT%{_appdefsdir},%{_desktopdir},%{_pixmapsdir}}

#rm $RPM_BUILD_ROOT%{_datadir}/freeciv/Freeciv

#install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
#install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/freeciv/stdsounds.soundspec
#cp -ar stdsounds $RPM_BUILD_ROOT%{_datadir}/freeciv

%find_lang freeciv 

%clean
rm -rf $RPM_BUILD_ROOT

%files -f freeciv.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/freeciv
#%%{_desktopdir}/*
#%%{_pixmapsdir}/*
