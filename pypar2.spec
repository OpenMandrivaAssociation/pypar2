%define realname PyPar2

Name:		pypar2
Version:	1.4
Release:	8
License:	GPL
Group:		File tools	
Summary:	Graphical frontend for the Linux par2 command line
URL:		http://pypar2.silent-blade.org/
Source0:	http://pypar2.silent-blade.org/uploads/Main/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	python, pygtk2.0-devel, pygtk2.0-libglade, python-pyxml, desktop-file-utils, python-vte
Requires:       pygtk2.0, pygtk2.0-libglade, parchive2, python-pyxml, python-vte

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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.4-7mdv2010.0
+ Revision: 430821
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-6mdv2009.0
+ Revision: 259451
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-5mdv2009.0
+ Revision: 247319
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-3mdv2008.1
+ Revision: 171056
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 29 2007 Emmanuel Andry <eandry@mandriva.org> 1.4-2mdv2008.0
+ Revision: 93875
- fix menu entry
- fix desktop validation
- fix permissions (bug #34299)

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix man pages

* Mon Apr 23 2007 Jérôme Soyer <saispo@mandriva.org> 1.4-1mdv2008.0
+ Revision: 17233
- New release 1.4


* Fri Mar 02 2007 Jérôme Soyer <saispo@mandriva.org> 1.3-2mdv2007.0
+ Revision: 131194
- Fix running

* Wed Feb 28 2007 Jérôme Soyer <saispo@mandriva.org> 1.3-1mdv2007.1
+ Revision: 126952
- Add BR
- Import pypar2

