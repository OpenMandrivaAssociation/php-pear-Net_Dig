%define		_class		Net
%define		_subclass	Dig
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.1
Release:	16
Summary:	Interface to the dig command
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Net_Dig/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The PEAR::Net_Dig class should be a nice, friendly OO interface to the
dig command.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-14mdv2012.0
+ Revision: 742140
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-13
+ Revision: 679412
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-12mdv2011.0
+ Revision: 613723
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-11mdv2010.1
+ Revision: 468692
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1-10mdv2010.0
+ Revision: 441412
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1-9mdv2009.1
+ Revision: 322377
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2009.0
+ Revision: 236979
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.1-7mdv2008.1
+ Revision: 136412
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2007.0
+ Revision: 82274
- Import php-pear-Net_Dig

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdk
- initial Mandriva package (PLD import)

