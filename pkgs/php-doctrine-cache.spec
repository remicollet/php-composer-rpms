%{?composer_find_provides_and_requires}

%global github_owner     doctrine
%global github_name      cache
%global github_version   1.0
%global github_commit    914abe4a49f2eae2b268073cca147b530da0308a

%global composer_vendor  %{github_owner}
%global composer_project %{github_name}

Name:           php-%{composer_vendor}-%{composer_project}
Version:        %{github_version}
Release:        1%{?dist}
Summary:        Caching library offering an object-oriented API for many cache backends

License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  php-composer

# phpci
Requires:       php-reflection
Requires:       php-spl

%description
%{summary}.

Optional dependencies: apc, couchbase, memcache, memcached, redis, xcache

WARNING: This is just a development RPM.  Please submit issues at
         https://github.com/siwinski/php-composer-rpms/issues and prefix
         your issue title with "[%name] ".


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing to build


%install
%{composer_install} --verbose


%files
%doc *.md
%dir %{composer}/%{composer_vendor}
     %{composer}/%{composer_vendor}/%{composer_project}
%exclude %{composer}/%{composer_vendor}/%{composer_project}/*.md


%changelog
* Fri Apr 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
