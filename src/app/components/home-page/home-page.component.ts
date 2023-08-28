import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SupportService } from 'src/app/support.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {
  constructor(private support: SupportService, private router: Router) { }
  ngOnInit() {
    this.getPlatforms();
  }
  platforms = [{ name: "Try", icon: "try" }];
  getPlatforms() {
    this.platforms = this.support.getPlatforms();
  }
  setPlatform(pform: string) {
    this.support.setPlatform(pform);
    this.router.navigate(["/upload"]);
  }
}
