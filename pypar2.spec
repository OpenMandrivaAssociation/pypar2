%define realname PyPar2

Name:		pypar2
Version:	1.4
Release:	9
License:	GPL
Group:		File tools	
Summary:	Graphical frontend for the Linux par2 command line
URL:		http://pypar2.silent-blade.org/
Source0:	http://pypar2.silent-blade.org/uploads/Main/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pygtk2.0-devel
BuildRequires:	pygtk2.0-libglade
BuildRequires:	desktop-file-utils
BuildRequires:	python-vte
Requires:       pygtk2.0
Requires:       pygtk2.0-libglade
Requires:       parchive2
Requires:       python-vte

Requires(post): desktop-file-utils 
Requires(postun): desktop-file-utils

%description
PyPar2 is a graphical frontend for the Linux par2 command line, 
written in Python. Its GUI uses GTK through the PyGTK library.

PyPar2 is designed to be very easy to use. For this reason:

    * Advanced settings are present, but hidden by default.
    * There is no preferences dialog, all selected options 
      are automatically saved and restored. 

%prep
%setup -q -n %{realname}-%{version}

perl -pi -e "s!/usr/local!%{buildroot}/usr!g" Makefile

%build


%install
make install

perl -pi -e 's,%{name}.png,%{name},g' %{buildroot}%{_datadir}/applications/*

desktop-file-install --vendor="" \
  --add-category="System;Filesystem" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/pypar2.desktop

rm -f %{buildroot}/%{_bindir}/pypar2
echo "python /usr/share/pypar2/src/main.py" > %{buildroot}/%{_bindir}/pypar2

%find_lang %name

%files -f %name.lang
%{_datadir}/applications/pypar2.desktop
%{_mandir}/man1/pypar2.*
%{_datadir}/%{name}/res/*.glade
%{_datadir}/%{name}/src/*.py
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/pix/*.png
%defattr(755,root,root)
%{_bindir}/pypar2

